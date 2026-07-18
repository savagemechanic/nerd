<div align="center">

# 🤓 nerd

**The Agent Skill that makes your AI show its work.**

*Stop letting your agent hide behind abstractions. Force it to draw the actual machine.*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![lint](https://github.com/savagemechanic/nerd/actions/workflows/lint.yml/badge.svg)](https://github.com/savagemechanic/nerd/actions/workflows/lint.yml)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-standard-blueviolet.svg)](https://agentskills.io)
![No Dependencies](https://img.shields.io/badge/dependencies-zero-green.svg)
![Works Everywhere](https://img.shields.io/badge/works%20with-Claude%20Code%20%C2%B7%20Cursor%20%C2%B7%20Codex%20%C2%B7%20Pi%20%C2%B7%20Gemini%20CLI-orange.svg)

</div>

---

> **The problem**
> You ask your AI agent to explain a system. It replies:
>
> *"The service uses a resilient coordination layer that orchestrates peer discovery and reconciles desired state across the fleet."*
>
> You nod. You still don't know if there's a bug. **Because prose hides invariants. Diagrams expose them.**
>
> **The fix**
> `nerd` makes the agent redraw that sentence as boxes, arrows, and the literal data structures underneath — plus the **invariant** that, if broken, *is* your bug.

---

## 👀 What it looks like (the whole pitch)

**Before `nerd`** — your agent on a rate-limited login flow:

```
The authenticate function validates credentials against the session store,
consults the rate limiter, and on success issues a signed token returned to
the caller for subsequent requests. Failed attempts increment a counter...
```

🥱 *Nods. Still can't see the race condition.*

**After `/skill:nerd`** — same code, same agent, forced to be honest:

```
   POST /login {user, pass}
        │
        ▼
   ┌─────────────────────────────┐
   │ sessions  map[token]session │ ◄── hash map, keyed by token
   │ attempts  map[user]int      │ ◄── hash map, keyed by user
   └──────────────┬──────────────┘
                  ▼
        ┌─────────────────────┐
        │ attempts[user] >= 5 │ ──YES──► 429 lockout
        └─────────────────────┘
                  │ NO
                  ▼
        verify password ──fail──► attempts[user]++   ◄── ⚠️ NOT atomic
                  │ ok                              ⚠️ reads map, writes map,
                  ▼                                   two threads can both pass
        token = random()
        sessions[token] = {user, exp}
        attempts[user] = 0
                  │
                  ▼
              return token

  Invariant:  sessions[t].exp > now  AND  not revoked  ⟹ token valid
  ↑ when this breaks, that's your bug.
```

😬 *Oh. There it is.* That's the whole point.

---

## 🧠 Why it works — the three things `nerd` forces

Most "draw me a diagram" prompts fail because the agent cheats. `nerd` is a **discipline**, not a prompt. It enforces three rules the agent cannot weasel out of:

### 1. Literal data structures, never blobs
```
   ❌  ┌─────────┐
       │ System  │      ← banned. vague. useless.
       └─────────┘

   ✅  map[token]session      ← hash map: key=token, value=struct
       attempts map[user]int  ← hash map: key=user, value=counter
```
If the agent can't name the structure (hash map? ring buffer? trie? DAG?), **it doesn't understand it** and must go read the code.

### 2. The invariant goes on every diagram
An *invariant* is the rule that must hold before, during, and after the code runs. It's where correctness lives — and where bugs hide. Every `nerd` diagram ends with one, phrased as an assertion you could check:

> **Invariant:** *exactly one of {old key, new key} is live at any instant.*
> **Structural invariant (BST):** *left subtree < node < right subtree.*

Name the invariant → name the bug when it breaks.

### 3. Bird's-eye, then zoom — never a wall of text
`nerd` draws the map first, then **stops**. You drive the zoom:

```
  you: /skill:nerd src/auth/
  nerd: [big picture] → [per-flow diagrams] → [data-structure anatomy]
        → summary table → "want to zoom into anything?"

  you: go deeper on the rate limiter
  nerd: [expanded flowchart of just that, with complexity + failure modes]
```

---

## ⚡ Install (one line)

`nerd` follows the open [Agent Skills](https://agentskills.io) standard, so it works in **any** compatible harness. Drop the `nerd/` folder into your skills directory:

| Harness | Install command |
|---|---|
| **Pi** | `git clone https://github.com/savagemechanic/nerd.git ~/.pi/agent/skills/nerd` |
| **Claude Code** | `git clone https://github.com/savagemechanic/nerd.git ~/.claude/skills/nerd` |
| **Codex** | `git clone https://github.com/savagemechanic/nerd.git ~/.codex/skills/nerd` |
| **Cursor / Gemini CLI / other** | clone into whatever skills dir your tool scans |

Then `/reload` (or restart) and invoke it: **`/skill:nerd <anything>`**

> Prefer manual? Download `SKILL.md` + the `references/` folder — that's the whole skill. Zero dependencies. No build step. No network calls. It's just a disciplined prompt.

---

## 🎯 Usage

Point it at anything — a file, a folder, a design doc, a vague architecture question:

```
/skill:nerd src/payments/
/skill:nerd how does our cache invalidation work?
/skill:nerd docs/auth-design.md
```

It returns, in order:
1. **Big picture** — components + the boundaries between them
2. **One flowchart per flow** — every lifecycle, request path, mutation chain
3. **Data-structure anatomy** — the *fundamental nature* (hash map? graph? heap?) + what it represents in your code's vocabulary
4. **A summary table** — everything reduced to `nature | structure | invariant | one breath`

Then it offers zooms. Go deep on any single algorithm, data structure, or concept and it expands **only that node** — all the way to memory layout, operation costs, and failure modes.

### Zoom examples
```
you: zoom into the peer registry data structure
nerd: [it's a hash map] → [bucket layout diagram] → [the composite key] → 
      [O(1) get/put, collision chain] → [structural invariant: one record per key]

you: what's a nonce token, really?
nerd: [concept zoom] unguessable single-use bytes bound to a session — 
      not magic, just entropy + a one-time-use flag.
```

---

## 🧩 What's inside

```
nerd/
├── SKILL.md                    ← the discipline (frontmatter + instructions)
├── references/
│   └── dsa-taxonomy.md         ← deep-dive anatomy of 14 data structures
│                                  + 10 algorithm classes, each with its
│                                  invariant, layout, and cost
└── examples/
    └── ...                     ← real nerd outputs (proof it works)
```

The taxonomy is loaded **on-demand** only when you ask to zoom — so the bird's-eye pass stays cheap.

---

## 🆚 How is this different from just asking "draw me a diagram"?

| | "draw me a diagram" | `nerd` |
|---|---|---|
| Vague blobs allowed | ✅ yes, constantly | ❌ banned — must show real structures |
| Names the algorithm class | rarely | always (reconcile loop? upsert? atomic swap?) |
| States the invariant | never | on **every** diagram |
| Reads your actual code first | maybe | always — won't draw from memory |
| Drill-down | ask again, re-explain | recursive zoom into one node |
| Result | pretty picture | a map you can find bugs on |

A diagram without the invariant is decoration. `nerd` refuses to decorate.

---

## 💡 When to reach for it

- **"I inherited this codebase and don't understand it"** → point nerd at it, get the map in 30 seconds
- **"The agent's explanation sounds smart but I don't trust it"** → nerd forces literal structures; if it can't name them, it says so
- **"I think there's a race condition but I can't see it"** → the invariant line is usually where it surfaces
- **"Review this PR"** → get the before/after data-flow diff, not a vibe check
- **"Onboard a new engineer"** → hand them `/skill:nerd src/` and let them zoom themselves

---

## 🤝 Works with

`nerd` is harness-agnostic. It's just a `SKILL.md` + a reference doc following the [Agent Skills spec](https://agentskills.io/specification):

- ✅ **Pi** — `/skill:nerd`
- ✅ **Claude Code** — `/skill:nerd`
- ✅ **OpenAI Codex CLI** — `/skill:nerd`
- ✅ **Cursor** — load as a skill/rule
- ✅ **Gemini CLI** — load as a skill
- ✅ Anything that reads a `SKILL.md`

Don't see yours? If your tool loads markdown skill files, `nerd` already works.

---

## ⭐ Why star this

If you've ever read an agent's explanation, nodded along, and then **still couldn't tell if the code was correct** — this is the fix. Stars help other developers find it. And honestly: the diagrams look great in a screenshot. 🤓

---

## 📄 License

MIT — do whatever. Attribute if you feel like it. Build cooler things.

<div align="center">

*Made for people who'd rather see the hash map than hear about the "resilient layer."*

</div>
