# `nerd` launch campaign

The actual playbook. Read this before posting anything.

---

## Part 0 — The hard truth about "driving traffic"

Automated mass cross-posting **will get the repo labeled as spam and the posting account shadowbanned.** Reddit, HN, and X specifically detect:

- the same link dropped across many subs in a short window
- a low-karma / new account posting only self-promo
- coordinated upvoting (this is a bannable offense on every platform)

The repos that hit 1k stars don't win on post *volume*. They win because **one banger native post** in the right community hit the front page, and the repo *converted* the resulting visitors. `nerd` is built to convert (hero image, invariants, green CI). Your job is to land **one** great post per community, spaced out, with you genuinely in the comments. That's it.

> ⚠️ **Prerequisite check before you post.** If your Reddit/HN account is new or low-karma, your posts will be auto-removed by filters before anyone sees them. Spend a week upvoting/commenting genuinely in 2-3 target subs first (the 10:1 rule). An established account is worth 100× a new one for this.

---

## Part 1 — The persuasion principles in play (used honestly)

These aren't dark patterns — they're why good technical content travels. Each is applied to the copy below.

| Principle | How it's used in `nerd` |
|---|---|
| **Curiosity gap** | "You nodded… but you still don't know if it's right." Opens a loop the reader wants to close. |
| **Specificity = credibility** | A real invariant (`sessions[t].exp > now`), a real bug (`NOT atomic`). Vague claims get scrolled past; concrete ones get believed. |
| **Authority via substance** | The *invariant* concept signals real CS depth. Readers infer the maker knows what they're doing. |
| **Reciprocity** | Free, MIT, zero-deps, useful even if they never star. They star to repay the gift. |
| **Loss aversion** | "The bug lives in the invariant the prose hid." Frames not-using-it as risking undetected bugs. |
| **Authenticity > hype** | Technical communities reward "I made a thing, roast it" and punish "🚀 game-changing revolutionary." The whole brand is anti-hype. |
| **Identity / self-expression** | Starring = "I'm the kind of dev who values rigor over vibes." Make starring feel like a taste statement. |
| **Social proof seeding** | A few genuine early stars + comments create the momentum that makes strangers star. Never faked. |

---

## Part 2 — The content ladder (each platform gets NATIVE copy, not dupes)

One hero asset (the `assets/social-card.png` before/after) repurposed into platform-native pieces. **Do not paste the same body everywhere** — that's the spam signal.

### 🟧 Hacker News — the swing-for-the-fences post
*When: Tue–Thu, 8–10am ET. Title is everything; keep it understated.*

**Title:** `Show HN: nerd – an agent skill that makes your AI explain code with the actual data structures and invariants`

**Body (short, let the comments carry it):**

> I kept getting agent explanations that sounded right and left me unsure the code was correct — prose hides invariants, and the bug is always in the thing the prose glossed over.
>
> So I made a small skill called nerd. It's a discipline, not a prompt: when you point it at code it has to draw the literal data structures (the actual map, the linked list), name the algorithm class, and state the invariant on every diagram — phrased as an assertion you could check. When the invariant breaks, that's your bug.
>
> It follows the open Agent Skills standard, so it works in Claude Code, Cursor, Codex, Pi, Gemini CLI. One file, zero deps, MIT: https://github.com/savagemechanic/nerd
>
> Curious whether the "invariant on every diagram" framing resonates, or if it's just me who finds prose explanations untrustworthy. Roast welcome.

**Your first comment (post within 60 seconds of submitting) — the technical meat + the image:**

> Here's the example that made it click for me — a rate-limited login flow, before/after: [link to the social card image, or the README section]. The agent didn't volunteer "this isn't atomic" in prose; it surfaced it by being forced to draw the read-then-write. The invariant line at the bottom is the part I haven't seen any other "diagram it" prompt produce.

### 🟦 r/LocalLLaMA — the local-first, zero-dep angle
*This sub is technically literate and skeptical of hype. Lead with openness.*

**Title:** `I made an agent skill (zero deps, works with any local agent) that stops the model from explaining code in vibes — forces real data structures + the invariant where bugs live`

**Body:**

> You know the pattern: you ask the model to explain a system, get three confident paragraphs, and still can't tell if there's a race condition.
>
> nerd is a skill (just a SKILL.md + a reference doc, no deps, no API calls, MIT) that forces the opposite. Point it at code and it produces ASCII flowcharts with the literal data structures drawn in, names the algorithm class, and puts the invariant on every diagram — the assertion that, when violated, is the bug.
>
> Works with any agent that loads a skill file: Claude Code, Cursor, Codex, Pi, Gemini CLI, local agents included. Nothing phones home.
>
> [attach social-card.png]
>
> The "invariant on every diagram" part is the bit I'm proudest of — that's where correctness actually lives. Repo: https://github.com/savagemechanic/nerd
>
> Genuinely want feedback from people running local agents — does the framing land for you?

### 🟧 r/ChatGPTCoding — the pain-first angle
**Title:** `Got tired of my agent explaining code in prose I couldn't trust — made a skill that forces ASCII flowcharts + the invariant where bugs hide`

**Body:** same pain-led opening as the README, attach the card, one-line install, "does the invariant framing click or is it overkill?"

### 🟪 r/cursor — tool-specific, install-led
**Title:** `A skill that makes Cursor explain your codebase with ASCII flowcharts + invariants instead of prose`
**Body:** install one-liner for Cursor specifically, the before/after card, "useful for inheriting a codebase / PR review / onboarding."

### 🟨 r/ClaudeAI — Claude-specific
**Title:** `Made a Claude Code skill ("nerd") that makes it show its work — ASCII diagrams with the invariant where bugs live`
**Body:** `/skill:nerd src/auth/` example, install to `~/.claude/skills/nerd`, card attached.

### 🐦 X / Twitter — a 5-tweet thread (image on tweet 1)
1. *(image: social-card.png)* I got tired of my AI agent explaining code in prose that sounded right and left me unsure if it was actually right. So I made it show its work.
2. The bug is always in the thing the prose glossed over. Prose hides invariants. Diagrams expose them.
3. nerd is a skill that forces the agent to: draw the LITERAL data structures (the real map, the linked list — no vague blobs), name the algorithm class, and put the INVARIANT on every diagram.
4. The invariant is the assertion that must hold — and when it breaks, that's your bug. That's the part no other "diagram it" prompt does.
5. Works in Claude Code, Cursor, Codex, Pi, Gemini CLI. Zero deps, MIT. → https://github.com/savagemechanic/nerd

### 🐘 Mastodon / fedi — the open + anti-corporate angle
> Made a tiny agent skill called nerd. It refuses to let your AI explain a system in prose — it forces ASCII flowcharts with the real data structures drawn in, and the invariant (the rule whose violation is the bug) on every diagram.
>
> Open (MIT), zero deps, nothing phones home, works with any agent that loads a skill file — Claude Code, Cursor, Codex, Pi, Gemini, local agents.
>
> → https://github.com/savagemechanic/nerd
>
> The invariant part is the thing. Prose hides it; diagrams expose it.

### 📝 dev.to / your blog — the long-form slow burn (highest SEO value)
**Title:** `How I made my AI agent stop lying to me about code (with invariants)`

The story arc: the problem (untrustworthy prose explanations) → why prose fails (it hides invariants) → the three rules nerd enforces → a worked example → the invariant as a correctness tool → install. 800–1200 words. This is the piece that keeps bringing traffic for months via search. Publish 1–2 days after the social push so the repo already has social proof when blog readers arrive.

---

## Part 3 — The sequenced rollout (DO NOT post all at once)

Spacing is the difference between a launch and a ban. Suggested sequence over ~5 days:

| Day | Action | Why this order |
|---|---|---|
| **Day 0** | Prep: confirm your account has enough karma/age (else build it first). Have the card image ready. | Filters will kill a low-trust account. |
| **Day 1, AM ET** | **r/LocalLLaMA** (or r/ChatGPTCoding) — your most receptive audience. Be in the comments for 2 hours. | Seeds genuine stars/comments = social proof before the bigger swing. |
| **Day 1, evening** | **X thread** + **Mastodon** (different audiences, low overlap with Reddit). | Broadens reach without Reddit-duplicate penalty. |
| **Day 2** | Rest from posting. Reply to every comment. Star/follow people who engaged. | Reciprocity; keeps day-1 posts alive. |
| **Day 3, AM ET** | **Hacker News** Show HN — the big swing. First comment within 60s. Present for 3 hours. | You want HN to see an already-starred repo. |
| **Day 3 PM** | If HN is going well, **r/cursor** + **r/ClaudeAI** (different niches, spaced from day 1). | Ride the momentum; these subs don't overlap with LocalLLaMA. |
| **Day 4** | Publish the **dev.to long-form**. | Converts the long-tail; repo now has social proof. |
| **Day 5+** | Engage, don't repost. If a post flopped, do NOT delete-and-repost elsewhere same week. | Patience. Flops are normal. |

### The first-hour playbook (this is where stars are actually won)
The algorithm weights early engagement heavily. For every post:
- **Be online and replying within minutes** of every comment for the first 60–90 minutes.
- Have **2 prepared follow-up comments** of your own (the technical deep-dive + the image link) to seed discussion.
- **Thank people** who give feedback, even critical — visible responsiveness earns upvotes and stars.
- Never argue with a hater; "good point, here's why I did X" wins the room.

---

## Part 4 — The ban-triggers (do NOT do these)

- ❌ Posting the same link to 5 subs in one day.
- ❌ Asking friends/Discord to upvote (vote manipulation = instant ban, all platforms).
- ❌ A new/low-karma account posting only self-promo.
- ❌ Deleting a flopped post and reposting it.
- ❌ Bot/alt accounts for fake engagement. (Besides being fraud, the platforms catch it and the repo looks spammy to real visitors.)
- ❌ Hype words in titles ("revolutionary", "game-changing", "10x"). They suppress upvotes in technical communities.

---

## Part 5 — Repo-side amplification (already done via `gh`)

These are the legitimate, on-repo actions that signal "this is a real, maintained project" — which itself drives stars:

- ✅ **GitHub Release v0.1.0** created (see Releases) — gives the repo a Releases entry + tag + activity ping.
- ✅ **15 discoverability topics** on the repo.
- ✅ **Green CI** (lint workflow) — the "maintained" badge.
- ✅ **Hero image** committed + embedded above the README fold.
- ✅ **MIT license**, zero-dep, Agent Skills standard.

### Optional next repo-side moves (say the word)
- **Enable Discussions** + seed a "How are you using nerd?" thread (social proof surface).
- **Add a CONTRIBUTING.md** + issue templates (signals serious project → more stars from drive-by visitors).
- **Pin an issue** with a quickstart / "star if this resonates" (the explicit ask — many people star only when asked).

---

## The one-sentence strategy

**Land one genuinely great, community-native post with you present in the comments; the repo (hero image + invariants + green CI) does the converting. Don't spam — participate.**
