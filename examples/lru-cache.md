# Example: `/skill:nerd` on an LRU cache

A real `nerd` output, lightly trimmed. Shows the full arc: big picture → flow → data-structure anatomy → invariant → summary table → zoom offer.

> **Input:** `/skill:nerd` pointed at a least-recently-used cache implementation.

---

## Big picture

```
   caller
     │  get(k) / put(k,v)
     ▼
   ┌────────────────────────────────────────┐
   │  LRU Cache  (capacity = N)             │
   │  ┌──────────────┐   ┌──────────────┐   │
   │  │ hash map     │   │ doubly-linked │   │
   │  │ key → node   │   │ list (order)  │   │
   │  └──────┬───────┘   └──────┬────────┘   │
   │         └────────┬─────────┘            │
   │           node holds BOTH               │
   │           (key, value, prev, next)      │
   └────────────────────────────────────────┘
```

**Fundamental nature:** A **hash map + doubly-linked list hybrid** — the map gives O(1) lookup, the list gives O(1) recency reordering.

**Invariant:** The linked list is always ordered from most-recently-used (head) to least-recently-used (tail); every key in the map has exactly one node in the list, and vice versa.

---

## Flow — `get(k)`

```
   get(k)
     │
     ▼
   ┌──────────────────┐
   │ k in map?        │
   └──────────────────┘
      │ NO              │ YES
      ▼                 ▼
   return -1        node = map[k]
                    move node → head   ◄── O(1): unlink + prepend
                    return node.value
```

**Fundamental nature:** A **lookup followed by a relocate** — existence check via hash map, recency fix via list splice.

**Invariant (loop-free):** after `get(k)` returns a hit, `k`'s node is the list head.

---

## Flow — `put(k, v)`

```
   put(k, v)
     │
     ▼
   ┌──────────────────┐
   │ k in map?        │
   └──────────────────┘
      │ YES                 │ NO
      ▼                     ▼
   update node.value    add node at head
   move node → head     map[k] = node
                         │
                         ▼
                    ┌──────────────────┐
                    │ len(map) > cap?  │
                    └──────────────────┘
                       │ YES
                       ▼
                    evict tail node      ◄── least recently used
                    delete map[tail.key]
```

**Fundamental nature:** An **upsert with a capacity-gated eviction** — insert/update, then if over capacity, drop the tail (the LRU victim).

**Invariant:** after `put` returns, `len(map) <= capacity`, always.

---

## Data-structure anatomy — the node

```
   type node struct {
       key   string
       value any
       prev  *node   ◄── link to newer
       next  *node   ◄── link to older
   }

   head ◄──► [A] ◄──► [B] ◄──► [C] ◄──► tail
   most-recent                       least-recent  (eviction victim)
```

- **Nature:** a **doubly-linked list** — O(1) unlink from anywhere (no traversal to find predecessor).
- **Structural invariant:** for every node, `node.prev.next == node` and `node.next.prev == node`; head.prev and tail.next are nil.

**Why both structures?** The map alone can't tell you recency. The list alone can't find a key in O(1). Together: O(1) everything.

---

## Summary table

| Op | Nature | Structure | Invariant | One breath |
|---|---|---|---|---|
| `get` | lookup + relocate | map + DLL splice | hit ⇒ node is head | find it fast, then mark it fresh |
| `put` | upsert + gated evict | map + DLL + cap | len ≤ capacity | add it, then trim the oldest if full |
| node | doubly-linked record | {key,val,prev,next} | links are symmetric | holds key+value+two pointers |

---

## Want to zoom?

1. **The eviction path** — exactly how the tail is unlinked and freed
2. **Why doubly-linked, not singly** — the O(1) predecessor problem
3. **Thread safety** — what breaks if two goroutines `put` at once (the invariant above does)
4. **Java's `LinkedHashMap` trick** — the same idea in 3 lines using access-order mode
