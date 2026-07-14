# 🏹 DSA 2025 — The Master Battle Plan

> *"Yogasthah kuru karmani" — Established in focus, perform action.*
> — Bhagavad Gita 2.48

---

## Who This Plan Is For

**Language**: Python.
**Goal**: Crack technical interviews at top companies.
**Commitment**: Practice every day.
**AI Workflow**: Opus handles strategy & blueprints. Other models handle implementation & scaffolding.

---

## Table of Contents

1. [The Big Picture](#1-the-big-picture)
2. [Topic Priority Tiers](#2-topic-priority-tiers)
3. [The Topic Lifecycle — How We Conquer Each Topic](#3-the-topic-lifecycle)
4. [Daily Routine — The Discipline](#4-daily-routine)
5. [Weekly Rhythm](#5-weekly-rhythm)
6. [The Full Timeline — Week by Week](#6-the-full-timeline)
7. [Folder Structure & Conventions](#7-folder-structure--conventions)
8. [AI Workflow — Who Does What](#8-ai-workflow)
9. [The "Stuck" Protocol](#9-the-stuck-protocol)
10. [Progress Tracking System](#10-progress-tracking-system)
11. [Interview Readiness Checkpoints](#11-interview-readiness-checkpoints)
12. [Cross-Topic Pattern Map](#12-cross-topic-pattern-map)

---

## 1. The Big Picture

There are **21 topics** across **6 phases** in your roadmap. But not all topics
are equally important for interviews. The plan is designed around this reality:

- **Phase 1-2 (Topics 1-6)**: The bread and butter. 60%+ of interview questions
  come from these patterns.
- **Phase 3 (Topics 7-10)**: Trees and heaps. The "must be comfortable" zone.
- **Phase 4 (Topics 11-13)**: Graphs. High-value, medium-frequency.
- **Phase 5 (Topics 14-17)**: The advanced arsenal. DP and Binary Search are
  heavy hitters.
- **Phase 6 (Topics 18-21)**: Specialized topics. Nice-to-have, rarely decisive.

**Your existing repo already has `notes.md` and `practice_problems.md` for
every single topic.** That's a huge head start. The plan leverages this.

---

## 2. Topic Priority Tiers

### 🔴 Tier 1 — Non-Negotiable (Must Be Excellent)

These topics cover ~80% of interview questions. Master these cold.

| # | Topic | Duration | Why Critical |
|---|-------|----------|-------------|
| 01 | Arrays & Strings | 1 week | Foundation of everything |
| 02 | Two Pointers | 3-4 days | Appears in 30%+ of problems |
| 03 | Sliding Window | 4-5 days | THE substring/subarray pattern |
| 04 | Hash Tables | 1 week | O(1) lookup — used everywhere |
| 05 | Linked Lists | 1 week | Pointer manipulation fundamentals |
| 06 | Stacks & Queues | 1 week | Nesting, matching, monotonic patterns |
| 07 | Binary Trees | 1.5 weeks | Recursion + tree traversals |
| 08 | BSTs | 1 week | Ordered data operations |
| 11 | Graphs (BFS/DFS) | 1 week | Connected components, shortest path |
| 14 | Binary Search | 1 week | Search space reduction |
| 16 | Dynamic Programming | 2.5 weeks | The boss battle |

### 🟡 Tier 2 — Strong Advantage

Asked somewhat frequently. Being good here differentiates you.

| # | Topic | Duration | Why Important |
|---|-------|----------|-------------|
| 09 | Heaps | 1 week | Top-K problems, merge K lists |
| 13 | Union Find | 4-5 days | Connected components (alternative to DFS) |
| 15 | Backtracking | 1.5 weeks | Combinatorics, permutations |
| 17 | Greedy | 1 week | Optimization without DP |
| 18 | Intervals | 4-5 days | Meeting rooms, merge intervals |

### 🟢 Tier 3 — Nice to Have

Rarely decisive in interviews. Study if time permits.

| # | Topic | Duration | When It Appears |
|---|-------|----------|----------------|
| 10 | Tries | 4-5 days | Autocomplete, word search |
| 12 | Advanced Graphs | 2 weeks | Dijkstra, Bellman-Ford (rare) |
| 19 | Bit Manipulation | 4-5 days | Single number, power of 2 |
| 20 | Math & Geometry | 1 week | Rarely, but can surprise you |
| 21 | Advanced DS | 1 week | Almost never in standard interviews |

> **Strategy**: Complete ALL Tier 1 first. Then Tier 2. Only touch Tier 3
> if you have time remaining or a specific company is known to ask them.

---

## 3. The Topic Lifecycle

Every topic follows the **exact same 5-phase lifecycle**. No exceptions.
This is your factory assembly line.

### Phase A: Learn (Day 1 of a topic)

**What happens:**
1. Read the existing `notes.md` for the topic.
2. Have a conversation with Opus about the core patterns.
3. Opus explains the patterns from scratch (like we did for Arrays —
   memory, Big-O, linear scan, two pointers, hash maps).
4. **Outcome**: You understand the *concept* before touching any code.

**Who does it:** You + Opus (conversation, no code).

### Phase B: Scaffold (Day 1, after learning)

**What happens:**
1. Opus reads the topic's `practice_problems.md`.
2. Opus writes a detailed `topic_XX_scaffold_blueprint.md` in the
   `planning/` folder (like we did for Topic 01).
3. Sonnet/Gemini reads the blueprint and creates pristine `.py` templates
   in `{topic_folder}/solutions/templates/`.
4. Templates are copied to `self-solutions/v1/` for you to practice.

**Who does it:** Opus writes blueprint → Sonnet/Gemini creates files.

### Phase C: Solve (Days 2-5 of a topic)

**What happens:**
1. You open files from `self-solutions/v1/` one by one.
2. You write the brute force first, then optimize.
3. You run the file: `python3 XX_problem_name.py`
4. If stuck, you use the "Stuck Protocol" (see Section 9).
5. If tests pass, you paste code for review.

**Who does it:** YOU. This is where the muscle memory builds.

**Target pace:**
- Easy problems: 15-20 minutes each
- Medium problems: 25-35 minutes each
- If you're spending 45+ minutes, you're stuck → use the protocol

### Phase D: The Wild (Days 5-6 of a topic)

**What happens:**
1. You go to LeetCode / NeetCode.
2. You solve 3-5 problems from the same topic WITHOUT any scaffolding.
3. No hints, no walkthroughs, no AI help. Just you and the problem.
4. This tests if you can recognize the pattern from a blank page.

**Who does it:** YOU alone on LeetCode.

### Phase E: Mock Interview (Day 7 — Final day of a topic)

**What happens:**
1. Opus gives you a random unseen problem from the topic.
2. You set a 30-minute timer.
3. You explain your thought process OUT LOUD (or in text) while coding.
4. Opus grades you on:
   - Did you identify the right pattern?
   - Is your code correct?
   - Did you handle edge cases?
   - Did you discuss time/space complexity?
   - Was your communication clear?

**Who does it:** You + Opus (simulated interview).

---

## 4. Daily Routine

### Weekday Schedule (Mon-Fri)

```
┌─────────────────────────────────────────────────────┐
│  DAILY DSA ROUTINE                                  │
├─────────────────────────────────────────────────────┤
│  [15 min] — Review yesterday's problems mentally    │
│             (Can you recall the pattern? The key    │
│              insight? The time complexity?)          │
│                                                     │
│  [60-90 min] — Solve 2-3 new problems from v1/     │
│                (brute force → optimized → run tests)│
│                                                     │
│  [15 min] — Review & reflect                        │
│             (What pattern did I use? Where did I     │
│              get stuck? What will I remember?)       │
└─────────────────────────────────────────────────────┘
```

### Rules:
1. **Always solve brute force first.** Even if you know the optimal. This
   proves to the interviewer you can think systematically.
2. **Set a timer.** If you can't solve a problem in 35 minutes, use the
   Stuck Protocol — don't waste time spinning.
3. **Remove your debug prints** before moving to the next problem. Keep
   your v1 files clean.
4. **Write a one-line comment** at the top of each solved function:
   `# KEY INSIGHT: ...` — this is your future-self's cheat sheet.

---

## 5. Weekly Rhythm

```
Monday    → New problems (2-3 scaffolded problems)
Tuesday   → New problems (2-3 scaffolded problems)
Wednesday → New problems (2-3 scaffolded problems)
Thursday  → New problems (2-3 scaffolded problems) — finish scaffolded set
Friday    → LeetCode "Wild" practice (3-5 unscaffolded problems)
Saturday  → Review week's problems + re-solve any you struggled with
Sunday    → Mock interview with Opus OR rest day
```

**On Review Days (Saturday):**
- Go back through your v1/ folder for the week
- For any problem where you used the Stuck Protocol, re-solve it from scratch
- Time yourself — are you faster this time?

---

## 6. The Full Timeline

### 📅 Phase 1: Foundations (Weeks 1-4)

| Week | Topic | # Problems | Focus |
|------|-------|-----------|-------|
| Week 1 | 01 - Arrays & Strings | 20 | Linear scan, Two pointers, Hash maps |
| Week 2 | 02 - Two Pointers | ~15 | Converging, fast-slow, read-write |
| Week 3 | 03 - Sliding Window | ~15 | Fixed window, variable window |
| Week 4 | 04 - Hash Tables | ~15 | Frequency maps, grouping, existence |

> **Checkpoint 1:** After Week 4, you should be able to solve any Easy
> array/string problem in under 15 minutes and most Medium ones in under 30.

---

### 📅 Phase 2: Linear Data Structures (Weeks 5-7)

| Week | Topic | # Problems | Focus |
|------|-------|-----------|-------|
| Week 5 | 05 - Linked Lists | ~15 | Pointer manipulation, fast-slow |
| Week 6 | 06 - Stacks & Queues | ~15 | Matching, monotonic, BFS queues |
| Week 7 | Review & consolidate Phase 1+2 | Mixed | Re-solve weak areas, mock interviews |

> **Checkpoint 2:** After Week 7, Phase 1-2 patterns should be automatic.
> You shouldn't need to "think" about Two Pointers — it should be instinct.

---

### 📅 Phase 3: Non-Linear Data Structures (Weeks 8-12)

| Week | Topic | # Problems | Focus |
|------|-------|-----------|-------|
| Week 8-9 | 07 - Binary Trees | ~20 | Recursion, DFS, BFS, traversals |
| Week 10 | 08 - BSTs | ~15 | Inorder property, validation |
| Week 11 | 09 - Heaps | ~12 | Top-K, merge, priority queues |
| Week 12 | 10 - Tries (if time) | ~8 | Prefix search, word dictionaries |

> **Checkpoint 3:** You should be comfortable with tree recursion. If someone
> says "binary tree" you should immediately think DFS/BFS.

---

### 📅 Phase 4: Graph Theory (Weeks 13-16)

| Week | Topic | # Problems | Focus |
|------|-------|-----------|-------|
| Week 13 | 11 - Graphs (BFS/DFS) | ~15 | Grid problems, connected components |
| Week 14-15 | 12 - Advanced Graphs | ~12 | Shortest path, topological sort |
| Week 16 | 13 - Union Find | ~8 | Dynamic connectivity |

> **Checkpoint 4:** Graph problems should feel like tree problems with
> extra edges. You should be able to set up adjacency lists from scratch.

---

### 📅 Phase 5: Advanced Techniques (Weeks 17-22)

| Week | Topic | # Problems | Focus |
|------|-------|-----------|-------|
| Week 17 | 14 - Binary Search | ~15 | Search space, boundary finding |
| Week 18-19 | 15 - Backtracking | ~15 | Subsets, permutations, N-Queens |
| Week 20-22 | 16 - Dynamic Programming | ~25 | 1D, 2D, knapsack, LCS, LIS |
| Week 22 | 17 - Greedy | ~10 | Activity selection, huffman-like |

> **Checkpoint 5:** DP is the hardest topic. After Week 22, you should be
> able to identify DP problems and set up state transitions for 1D/2D cases.

---

### 📅 Phase 6: Specialized Topics (Weeks 23-26)

| Week | Topic | # Problems | Focus |
|------|-------|-----------|-------|
| Week 23 | 18 - Intervals | ~8 | Merge, insert, meeting rooms |
| Week 24 | 19 - Bit Manipulation | ~8 | XOR tricks, single number |
| Week 25 | 20 - Math & Geometry | ~8 | GCD, primes, matrix rotation |
| Week 26 | 21 - Advanced DS | ~5 | Segment trees (overview only) |

> **Checkpoint 6:** You're interview-ready. Time to do full mock interviews
> mixing topics randomly.

---

## 7. Folder Structure & Conventions

Every topic folder follows this exact structure:

```
dsa-2025/
├── planning/                          ← Opus writes blueprints here
│   ├── master_plan.md                 ← THIS file (the master strategy)
│   ├── topic_01_scaffold_blueprint.md ← Blueprint for Topic 01
│   ├── topic_02_scaffold_blueprint.md ← Blueprint for Topic 02
│   └── ...
│
├── 01-arrays-strings/                 ← One folder per topic
│   ├── notes_arrays.md                ← Pre-existing theory notes
│   ├── notes_strings.md               ← Pre-existing theory notes
│   ├── practice_problems.md           ← Pre-existing problem list
│   └── solutions/
│       ├── templates/                 ← Pristine scaffolds (NEVER edit)
│       │   ├── _template.py
│       │   ├── pattern_cheatsheet.md
│       │   ├── 01_find_max.py
│       │   ├── 02_reverse_string.py
│       │   └── ...20 files
│       └── self-solutions/            ← YOUR practice space (git-ignored)
│           ├── .gitignore
│           ├── README.md
│           ├── v1/                    ← First attempt
│           │   ├── 01_find_max.py     ← You write code here
│           │   └── ...
│           └── v2/                    ← Re-attempt (weeks later)
│               └── ...
│
├── 02-two-pointers/                   ← Same structure repeats
│   ├── notes.md
│   ├── practice_problems.md
│   └── solutions/
│       ├── templates/
│       └── self-solutions/
│           └── v1/
│
└── ...21 topic folders total
```

### File Naming Convention
- Problem files: `{number:02d}_{snake_case_name}.py` (e.g., `03_two_sum.py`)
- Each file is self-contained and runnable: `python3 03_two_sum.py`
- Tests use `assert` statements — green `✅` or red `AssertionError`

---

## 8. AI Workflow — Who Does What

### Opus (The Strategist)
- Teaches patterns and concepts from scratch before each topic
- Writes `topic_XX_scaffold_blueprint.md` files
- Reviews your code like an interviewer
- Conducts mock interviews
- Gives "nudge hints" when you're stuck (never full solutions)
- Writes this master plan and updates it

### Sonnet / Gemini (The Builder — The Army)
- Reads blueprint files and creates `.py` template scaffolds
- Copies files to `self-solutions/v1/`
- Handles repetitive file creation tasks
- Runs commands (git, file operations)

### You (The Warrior)
- Reads the notes and learns the patterns
- Writes ALL the actual solution code
- Runs and debugs your own code
- Goes to LeetCode for wild practice
- Tracks your own progress

### The Handoff Flow
```
1. Opus teaches you the topic       (conversation)
2. Opus writes the blueprint        (planning/topic_XX_scaffold_blueprint.md)
3. You switch to Sonnet/Gemini      (model switch)
4. Sonnet creates template files    (solutions/templates/)
5. Sonnet copies to v1/             (solutions/self-solutions/v1/)
6. You switch back to Opus          (model switch)
7. You solve problems               (self-solutions/v1/)
8. Opus reviews your code           (conversation)
9. Repeat for next topic
```

---

## 9. The "Stuck" Protocol

When you've been staring at a problem for 15+ minutes without progress:

### Level 1 — Self-Help (Try first)
1. Re-read the pattern tag at the top of the file
2. Re-read the hints in the docstring
3. Walk through the example by hand on paper/mentally
4. Ask yourself: "What data structure would let me avoid the inner loop?"

### Level 2 — Ask Opus for a Nudge
Tell me specifically:
> *"I'm stuck on Problem X. I think I need [pattern] but I'm not sure
> about [specific thing]."*

I will give you a conceptual nudge — NOT the code. Example:
> *"You're right that you need a hash map. Think about what you're
> storing as the KEY vs the VALUE. What would let you look up the
> answer in O(1)?"*

### Level 3 — Guided Walkthrough
If Level 2 doesn't unblock you after another 10 minutes:
> *"I'm still stuck. Can you walk me through the first 3 steps
> of the algorithm?"*

I will trace through the example step by step, showing what happens
at each iteration, but I will NOT give you the final code.

### Level 4 — Study the Pattern
If you're completely lost on the fundamental pattern:
> *"I don't understand [Sliding Window / DP / etc.] at all. Teach me."*

We'll step back and I'll explain the pattern from first principles
before you attempt the problem again.

> **NEVER skip to "just give me the answer."** The pain of being stuck
> is where the learning happens. Every minute you struggle is a minute
> your brain is building neural pathways.

---

## 10. Progress Tracking System

### Per-Problem Tracking

After solving each problem, mentally rate yourself:

| Rating | Meaning | Action |
|--------|---------|--------|
| ⚡ Crushed it | Solved optimally in < 15 min | Move on |
| ✅ Solved | Solved optimally, took some time | Move on |
| 🟡 Struggled | Needed hints or multiple attempts | Re-solve on Saturday |
| 🔴 Failed | Couldn't solve even with hints | Study the pattern, re-solve in v2 |

### Per-Topic Tracking

At the end of each topic, assess yourself:

- **Green**: I can solve any medium problem in this topic in 25 min → Move on
- **Yellow**: I can solve most but struggle with some → Spend 1 extra day
- **Red**: I struggle with the core pattern → Spend 2-3 extra days before moving on

### Monthly Review

Every 4 weeks, go back and re-solve 5 random problems from previous topics.
If you can't solve them quickly, that topic needs revision.

---

## 11. Interview Readiness Checkpoints

### Checkpoint A — After Phase 2 (Week 7)
**Can you solve these types in under 25 minutes?**
- Two Sum, Three Sum
- Sliding window max/min
- Linked list reversal
- Valid parentheses (stack)

If YES → proceed. If NO → spend Week 7 on remediation.

### Checkpoint B — After Phase 3 (Week 12)
**Can you solve these types?**
- Binary tree traversals (all 4 types)
- BST validation
- Top-K elements with heap
- Level-order traversal (BFS)

### Checkpoint C — After Phase 5 (Week 22)
**Can you solve these types?**
- Graph DFS/BFS on grids
- Binary search on answer space
- Generate all subsets/permutations
- Basic 1D DP (climbing stairs, house robber, coin change)

### Checkpoint D — Final (Week 26)
**Full mock interview readiness:**
- Solve 2 medium problems in 45 minutes
- Explain your approach before coding
- Identify time/space complexity correctly
- Handle follow-up questions ("What if the input is sorted?")

---

## 12. Cross-Topic Pattern Map

Patterns don't live in isolation. Here's how they connect:

```
Arrays ──→ Two Pointers ──→ Sliding Window
  │              │                 │
  │              ├── Linked Lists (fast-slow pointer)
  │              └── Binary Search (left-right boundary)
  │
  ├── Hash Maps ──→ Frequency counting ──→ Sliding Window
  │              └── Grouping ──→ Graph adjacency lists
  │
  └── Stacks ──→ Monotonic Stack ──→ Next Greater Element
              └── DFS (recursive call stack)
                    │
                    ├── Binary Trees ──→ BSTs ──→ Heaps
                    │                        └── Tries
                    └── Graphs ──→ Topological Sort (Kahn's = BFS)
                                     └── Union Find
                                     
Binary Search ──→ DP (optimization over search space)
                └── Greedy (local optimal choice)

Backtracking ──→ DP (backtracking + memoization = DP)
```

**The golden insight:** Every advanced topic is built on a simpler one.
If you master Phase 1-2, everything after that is just combining patterns
you already know in new ways.

---

## What's Next — Immediate Actions

1. **Right now**: Continue solving Topic 01 problems in `self-solutions/v1/`
   (you're on Problem 4 — Valid Anagram).
2. **When Topic 01 is done**: Tell Opus. We'll do the Phase D (LeetCode wild)
   and Phase E (mock interview).
3. **Then**: Opus writes `topic_02_scaffold_blueprint.md`, teaches you
   Two Pointers in depth, and the cycle repeats.

---

*Remember, Parth — the goal isn't speed. It's depth. One problem truly
understood is worth ten problems copy-pasted. Trust the process.* 🏹
