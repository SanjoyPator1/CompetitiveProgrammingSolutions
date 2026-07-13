# 🧠 DSA 2025 — AI Context Handoff Document

> **PURPOSE**: Copy-paste the relevant sections of this file into any new AI
> chat session to give it full context about this project. This is the single
> source of truth for any model (Opus, Sonnet, Gemini) working on this repo.

---

## About

Doing a complete DSA revision to crack technical interviews.
Language: **Python**. Practice every day.

---

## Project Structure

```
dsa-2025/
├── Readme.md                          ← Full 21-topic roadmap (6 phases, ~26 weeks)
├── planning/
│   ├── master_plan.md                 ← The master strategy document (READ THIS FIRST)
│   ├── ai_context.md                  ← THIS file
│   └── topic_XX_scaffold_blueprint.md ← Detailed scaffolding specs per topic
│
├── {topic_folder}/                    ← e.g., 01-arrays-strings/
│   ├── notes.md (or notes_*.md)       ← Pre-existing theory notes
│   ├── practice_problems.md           ← Pre-existing problem list (15-20 problems)
│   └── solutions/
│       ├── templates/                 ← Pristine scaffold .py files (NEVER modify)
│       │   ├── _template.py           ← Base template format
│       │   ├── pattern_cheatsheet.md  ← Quick pattern reference
│       │   └── XX_problem_name.py     ← Individual problem scaffolds
│       └── self-solutions/            ← My practice space (git-ignored)
│           ├── .gitignore
│           ├── README.md
│           └── v1/                    ← Current attempt (copied from templates/)
│               └── XX_problem_name.py ← I write my code here
```

---

## How the Workflow Works

### The Topic Lifecycle (same for every topic)
1. **Learn** — Opus teaches patterns from scratch (conversation only)
2. **Scaffold** — Opus writes a blueprint → Sonnet/Gemini creates .py templates
3. **Solve** — I write code in `self-solutions/v1/`, run tests with `python3`
4. **Wild** — I solve 3-5 problems on LeetCode without scaffolds
5. **Mock** — Opus gives me a mock interview on the topic

### AI Role Division
- **Opus**: Strategy, teaching, blueprints, code review, mock interviews
- **Sonnet/Gemini**: File creation, scaffolding, git operations, repetitive tasks

---

## Template File Format (How Scaffolds Look)

Every `.py` problem file follows this exact structure:
```
1. Box header with problem name
2. Metadata block (Difficulty, Pattern, LeetCode link, Key Insight, Time, Space)
3. Interview Tip (💡) and Pattern Recognition (🧠) notes
4. from typing import List
5. Brute force function with hints (body = pass)
6. Optimized function with hints + walkthrough example (body = pass)
7. Test cases with assert statements (basic + edge cases)
8. print("✅ All tests passed!") at the end
```

> **CRITICAL RULE**: ALL function bodies in templates must be `pass`.
> Do NOT write solutions. Only provide hints in docstrings.

For reference, see any existing template file like:
`dsa-2025/01-arrays-strings/solutions/templates/03_two_sum.py`

### File Naming Convention
`{number:02d}_{snake_case_name}.py` — e.g., `06_first_unique_char.py`

---

## Current Progress Tracker

Update this section as topics are completed:

| # | Topic | Status | Notes |
|---|-------|--------|-------|
| 01 | Arrays & Strings | 🟡 IN PROGRESS | Templates done (20 problems). Solving in v1. |
| 02 | Two Pointers | ⬜ NOT STARTED | notes.md and practice_problems.md exist |
| 03 | Sliding Window | ⬜ NOT STARTED | notes.md and practice_problems.md exist |
| 04 | Hash Tables | ⬜ NOT STARTED | notes.md and practice_problems.md exist |
| 05 | Linked Lists | ⬜ NOT STARTED | notes.md and practice_problems.md exist |
| 06 | Stacks & Queues | ⬜ NOT STARTED | notes.md and practice_problems.md exist |
| 07 | Binary Trees | ⬜ NOT STARTED | notes.md and practice_problems.md exist |
| 08 | BSTs | ⬜ NOT STARTED | notes.md and practice_problems.md exist |
| 09 | Heaps | ⬜ NOT STARTED | notes.md and practice_problems.md exist |
| 10 | Tries | ⬜ NOT STARTED | notes.md and practice_problems.md exist |
| 11 | Graphs (BFS/DFS) | ⬜ NOT STARTED | notes.md and practice_problems.md exist |
| 12 | Advanced Graphs | ⬜ NOT STARTED | notes.md and practice_problems.md exist |
| 13 | Union Find | ⬜ NOT STARTED | notes.md and practice_problems.md exist |
| 14 | Binary Search | ⬜ NOT STARTED | notes.md and practice_problems.md exist |
| 15 | Backtracking | ⬜ NOT STARTED | notes.md and practice_problems.md exist |
| 16 | Dynamic Programming | ⬜ NOT STARTED | notes.md and practice_problems.md exist |
| 17 | Greedy | ⬜ NOT STARTED | notes.md and practice_problems.md exist |
| 18 | Intervals | ⬜ NOT STARTED | notes.md and practice_problems.md exist |
| 19 | Bit Manipulation | ⬜ NOT STARTED | notes.md and practice_problems.md exist |
| 20 | Math & Geometry | ⬜ NOT STARTED | notes.md and practice_problems.md exist |
| 21 | Advanced DS | ⬜ NOT STARTED | notes.md and practice_problems.md exist |

---

## How to Use This File in a New Chat

### Starting a new chat for SCAFFOLDING a topic:

> *Copy-paste this:*
>
> I'm doing a DSA revision journey. Read the following files for full context:
>
> 1. `dsa-2025/planning/ai_context.md` — Project context and conventions
> 2. `dsa-2025/planning/master_plan.md` — The full strategy
> 3. `dsa-2025/planning/topic_XX_scaffold_blueprint.md` — Blueprint for this topic
> 4. `dsa-2025/01-arrays-strings/solutions/templates/03_two_sum.py` — Format reference
>
> **TASK**: We are scaffolding **Topic XX: [Topic Name]**. Read the blueprint
> and create all the .py template files in `dsa-2025/{topic_folder}/solutions/templates/`.
> Then copy them to `dsa-2025/{topic_folder}/solutions/self-solutions/v1/`.
> Also create the `.gitignore` and `README.md` in `self-solutions/`.

---

### Starting a new chat for LEARNING a topic:

> *Copy-paste this:*
>
> I'm doing a DSA revision journey. Read the following files for full context:
>
> 1. `dsa-2025/planning/ai_context.md` — Project context and conventions
> 2. `dsa-2025/planning/master_plan.md` — The full strategy
> 3. `dsa-2025/{topic_folder}/notes.md` — Theory notes for this topic
> 4. `dsa-2025/{topic_folder}/practice_problems.md` — Problem list
>
> **TASK**: We are starting **Topic XX: [Topic Name]**. Teach me the core
> patterns from scratch as if I'm learning fresh. Then write a detailed
> `topic_XX_scaffold_blueprint.md` in `dsa-2025/planning/`.

---

### Starting a new chat for CODE REVIEW:

> *Copy-paste this:*
>
> I'm doing a DSA revision journey. Read the following files for full context:
>
> 1. `dsa-2025/planning/ai_context.md` — Project context and conventions
> 2. `dsa-2025/{topic_folder}/solutions/templates/XX_problem.py` — The original template
>
> **TASK**: Review my solution code below. Grade me like an interviewer:
> - Is the pattern correct?
> - Is the code clean and Pythonic?
> - Did I handle edge cases?
> - What's the time/space complexity?
> - Would this pass in a real interview?
>
> [paste your code here]

---

### Starting a new chat for MOCK INTERVIEW:

> *Copy-paste this:*
>
> I'm doing a DSA revision journey. Read the following files for full context:
>
> 1. `dsa-2025/planning/ai_context.md` — Project context and conventions
> 2. `dsa-2025/planning/master_plan.md` — The full strategy
>
> **TASK**: Give me a mock interview for **Topic XX: [Topic Name]**. Pick a
> problem I haven't seen before. I'll have 30 minutes. Act as a real
> interviewer — ask me to explain my approach before coding, ask follow-up
> questions, and grade me at the end.

---

## Key Rules for Any AI Working on This Project

1. **NEVER write solution code in template files.** Function bodies must be `pass`.
2. **Templates go in `solutions/templates/`.** They are pristine and committed to git.
3. **My practice code goes in `solutions/self-solutions/v1/`.** It is git-ignored.
4. **Follow the existing file format exactly.** Look at `03_two_sum.py` as reference.
5. **Each .py file must be self-contained and runnable** with `python3 filename.py`.
6. **Include both brute force and optimized approaches** with hints in docstrings.
7. **Include comprehensive test cases** with basic cases and edge cases labeled.
8. **Update the progress tracker** in this file when a topic changes status.
