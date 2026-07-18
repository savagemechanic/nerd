#!/usr/bin/env python3
"""
Validate a skill against the Agent Skills frontmatter contract.

Dependency-free. Designed to run in GitHub Actions on ubuntu-latest.
Checks:
  - SKILL.md exists and has a YAML frontmatter block
  - `name` is present and well-formed (lowercase, hyphens ok, 1-64 chars,
    no leading/trailing/consecutive hyphens)
  - `description` is present and <= 1024 chars
  - any references/... and examples/... paths mentioned in SKILL.md exist
  - README.md and LICENSE exist (release hygiene)

Exits non-zero on any failure. Prints a readable report.
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]  # repo root (scripts/ is 1 level under .github)
SKILL = ROOT / "SKILL.md"
MAX_NAME = 64
MAX_DESC = 1024
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")

errors: list[str] = []
checks: list[str] = []


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    """Parse a flat `key: value` frontmatter block. Returns (map, body)."""
    if not text.startswith("---"):
        return {}, text
    try:
        end = text.index("\n---", 3)
    except ValueError:
        return {}, text
    block = text[3:end].strip("\n")
    body = text[end + 4:].lstrip("\n")
    out: dict[str, str] = {}
    for line in block.splitlines():
        line = line.rstrip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        out[key.strip()] = val.strip().strip('"').strip("'")
    return out, body


def main() -> int:
    # --- required files ---
    for required in ("SKILL.md", "README.md", "LICENSE"):
        if not (ROOT / required).exists():
            errors.append(f"missing required file: {required}")
        else:
            checks.append(f"found {required}")

    if not SKILL.exists():
        # already reported above; bail
        return report()

    text = SKILL.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(text)

    if not fm:
        errors.append("SKILL.md has no parseable frontmatter block (--- ... ---)")
        return report()
    checks.append("frontmatter block present")

    # --- name ---
    name = fm.get("name", "")
    if not name:
        errors.append("`name` is required")
    else:
        if len(name) > MAX_NAME:
            errors.append(f"`name` length {len(name)} > {MAX_NAME}")
        if not NAME_RE.match(name):
            errors.append(
                f"`name` '{name}' must be lowercase letters/digits/hyphens, "
                "no leading/trailing/consecutive hyphens"
            )
        else:
            checks.append(f"`name` = '{name}' is well-formed")

    # --- description ---
    desc = fm.get("description", "")
    if not desc:
        errors.append("`description` is required (skill will not load without it)")
    else:
        if len(desc) > MAX_DESC:
            errors.append(f"`description` length {len(desc)} > {MAX_DESC}")
        else:
            checks.append(f"`description` present ({len(desc)} chars)")

    # --- referenced asset integrity ---
    # find anything that looks like a repo-relative path in the body
    ref_re = re.compile(r"(?:references|examples)/[A-Za-z0-9_./-]+\.md")
    seen = set()
    for m in ref_re.findall(body):
        candidate = m.rstrip("./")
        if candidate in seen:
            continue
        seen.add(candidate)
        target = ROOT / candidate
        if target.exists():
            checks.append(f"referenced asset exists: {candidate}")
        else:
            errors.append(f"SKILL.md references missing file: {candidate}")

    return report()


def report() -> int:
    print("== nerd skill validation ==")
    for c in checks:
        print(f"  \u2713 {c}")
    if errors:
        print("\nFAILED:")
        for e in errors:
            print(f"  \u2717 {e}")
        return 1
    print("\nAll checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
