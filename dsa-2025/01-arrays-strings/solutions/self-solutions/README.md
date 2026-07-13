# DSA 2025 — Self Solutions Workflow

## How to Use This Folder

The `solutions/templates/` folder contains **pristine scaffold files** — templates with hints
and test cases but empty function bodies. **Never solve directly in those files.**

This folder (`self-solutions/`) is your personal practice space.
It is git-ignored — your attempts stay private.

---

## Workflow for Each Practice Round

### Starting a New Attempt

```bash
# Create a new version folder (v1 for first attempt, v2 for second, etc.)
mkdir -p dsa-2025/01-arrays-strings/solutions/self-solutions/v1

# Copy ALL scaffold files into your version folder
cp dsa-2025/01-arrays-strings/solutions/templates/*.py \
   dsa-2025/01-arrays-strings/solutions/self-solutions/v1/
```

### Solving

```bash
# Open a problem and fill in the function bodies
code dsa-2025/01-arrays-strings/solutions/self-solutions/v1/03_two_sum.py

# Run it to check your solution
python3 dsa-2025/01-arrays-strings/solutions/self-solutions/v1/03_two_sum.py
# → ✅ All tests passed!   (or shows which assert failed)
```

### When to Create v2

Create `v2/` when:
- You want to re-attempt a topic from scratch after a few weeks
- You want to try a different approach (e.g., first attempt brute force, v2 optimal)
- Topic review on weekends

---

## Folder Structure (after a few rounds)

```
self-solutions/
├── README.md          ← this file
├── v1/                ← first attempt (current)
│   ├── 01_find_max.py
│   ├── 02_reverse_string.py
│   └── ...
├── v2/                ← re-attempt after 2-3 weeks
│   └── ...
└── v3/                ← pre-interview revision
    └── ...
```

---

## Tips

- **Don't peek at v1 when doing v2** — let your brain work fresh
- **Time yourself** — aim for ~25 min per medium problem
- **Write comments** — explain your thought process, not just code
- **Compare v1 vs v2** — track how much faster and cleaner you get
