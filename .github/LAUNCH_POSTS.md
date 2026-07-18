# Launch posts — `nerd`

Copy-paste drafts for seeding the discovery loop. Written in the repo's voice: honest, anti-jargon, leads with the before/after. Tweak the tone per community.

> Replace `https://github.com/savagemechanic/nerd` links if you cross-post under a different account. Screenshots of the ASCII output outperform text links — grab one from `examples/lru-cache.md` or the README.

---

## Hacker News — Show HN

**Title:** Show HN: nerd – an agent skill that forces your AI to explain code with real data structures and invariants

**Body:**

I kept running into the same problem: I'd ask an AI agent to explain a codebase or a system, get back a confident wall of prose ("it uses a resilient coordination layer that reconciles desired state..."), nod along, and still have no idea whether the code was actually correct. Prose hides invariants. The bug is always in the thing the prose glossed over.

So I made a small agent skill called **nerd**. It's not a prompt — it's a discipline the agent has to follow. When you point it at code, it has to produce:

1. ASCII flowcharts with the **literal data structures** drawn in (the actual `map[K]V`, the linked list, the ring buffer) — vague blobs are banned.
2. The **invariant** on every diagram: the assertion that must hold before/during/after, phrased so you could `assert()` it. When the invariant breaks, that's your bug.
3. A bird's-eye map, then it stops and lets you zoom into any single algorithm or data structure recursively.

Example. A rate-limited login flow:

```
   verify password ──fail──► attempts[user]++   ◄── NOT atomic
                                                  two threads can both pass
```

Invariant: `sessions[t].exp > now AND not revoked ⟹ token valid`.

The agent didn't volunteer "this isn't atomic" in prose. It surfaced it by being forced to draw the read-then-write.

It follows the open Agent Skills standard, so it works in Claude Code, Cursor, Codex, Pi, Gemini CLI — anywhere that loads a `SKILL.md`. Zero dependencies, one file plus a reference doc that loads on demand.

It's MIT, it's here: https://github.com/savagemechanic/nerd

I'm curious whether the "invariant on every diagram" framing resonates with anyone else, or if it's just me who finds prose explanations untrustworthy. Roast welcome.

---

## r/ChatGPTCoding / r/LocalLLaMA

**Title:** I made an agent skill that stops the AI from explaining things in vibes — it forces ASCII flowcharts + the invariant where bugs hide

**Body:**

You know the feeling: you ask the model to explain a system, it writes three paragraphs that sound smart, and you still can't tell if there's a race condition.

I wrote a skill called **nerd** (works with Claude Code, Cursor, Codex, Pi, Gemini CLI — it's just a `SKILL.md`). Three rules it forces:

- **No vague blobs.** It has to draw the real data structure. `map[token]session`, not a box that says "Store".
- **Every diagram gets an invariant** — the rule that, when broken, is your bug. e.g. "exactly one of {old key, new key} is live at any instant."
- **Map first, then zoom.** Bird's-eye view, then you drill into any one algorithm/data structure and it expands only that.

Here's the same login flow before and after — [paste screenshot from README]

The invariant line is the part I haven't seen any other "diagram it" prompt do. That's where correctness actually lives.

Repo (MIT, no deps): https://github.com/savagemechanic/nerd

Genuinely want feedback — does the invariant framing click for you, or is it overkill?

---

## r/cursor

**Title:** A skill that makes Cursor explain your codebase with ASCII flowcharts + invariants (not prose)

**Body:**

Drop-in skill for Cursor (and Claude Code / Codex / Pi / Gemini — it's a standard `SKILL.md`). Point it at a file or folder and instead of a prose summary you get:

- the actual data structures drawn out (hash map? DAG? ring buffer? — it names the fundamental type)
- a flowchart per flow
- the **invariant** on each — the assertion that, if violated, is the bug

Then you can zoom: "go deeper on the cache invalidation" and it expands just that.

Useful for inheriting a codebase, PR review, onboarding. One-line install:

```
git clone https://github.com/savagemechanic/nerd.git <your skills dir>/nerd
```

Repo: https://github.com/savagemechanic/nerd

---

## r/ClaudeAI

**Title:** Made a Claude Code skill ("nerd") that makes it show its work — ASCII diagrams with the invariant where bugs hide

**Body:**

Claude is great at explaining things in a way that sounds right and leaves you unsure if the code is right. This skill forces the opposite: literal data structures, an ASCII flowchart per flow, and the **invariant** (the rule that must hold, and whose violation is the bug) on every diagram.

`/skill:nerd src/auth/` → big picture → per-flow flowcharts → data-structure anatomy → summary table → "want to zoom?"

Install:

```
git clone https://github.com/savagemechanic/nerd.git ~/.claude/skills/nerd
```

Works in Cursor/Codex/Pi/Gemini too (Agent Skills standard). MIT, zero deps: https://github.com/savagemechanic/nerd

The "invariant on every diagram" part is the bit I'm proudest of — curious if other Claude users find it as useful as I do for actually trusting an explanation.

---

## Short social / Mastodon / X

Made an agent skill called **nerd**. It refuses to let your AI explain a system in prose. It forces ASCII flowcharts with the real data structures drawn in — and the **invariant** on every diagram. The invariant is where the bug lives. Prose hides it; diagrams expose it.

Works in Claude Code, Cursor, Codex, Pi, Gemini CLI. MIT, zero deps.

→ https://github.com/savagemechanic/nerd

---

## Posting notes

- **Lead with a screenshot**, not the link. The ASCII output is the hook; the link is the conversion.
- **HN**: post Tuesday–Thursday ~8–10am ET. Title matters most; keep it descriptive, not clicky. Engage in comments within the first hour.
- **Reddit**: each sub once, space them out, never multi-post the same minute. r/ChatGPTCoding and r/LocalLLaMA are the highest-leverage for this. Read each sub's rules on self-promo (the 10:1 guideline).
- **First comment** on every post: the before/after screenshot + the install one-liner. Make the first thing repliers see be the goods.
- **Don't call it "viral" or "game-changing"** anywhere. The whole brand is *anti*-hype. Let the invariant do the selling.
