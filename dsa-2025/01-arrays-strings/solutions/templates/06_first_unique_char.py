"""
╔══════════════════════════════════════════════════════════════╗
║  Problem 6: First Unique Character                           ║
╚══════════════════════════════════════════════════════════════╝

Difficulty: Easy
Pattern:    #️⃣ Hash Map (frequency counting)
LeetCode:   https://leetcode.com/problems/first-unique-character-in-a-string/

Key Insight: Count frequencies first, then find the first char with count == 1.
Time:  O(n) → O(n)  (two passes — one to count, one to find)
Space: O(1) — at most 26 lowercase letters

💡 Interview Tip: Two-pass is fine here. Don't try to do it in one pass —
   it's actually harder and not necessary.

🧠 Pattern Recognition: "Find first/last element with specific frequency"
   = frequency map + second scan.
"""

from typing import List


def first_unique_brute(s: str) -> int:
    """
    Approach: For each character, check if it appears elsewhere.

    Hints:
    - For each index i, scan rest of string for duplicates
    - Time: O(n²), Space: O(1)

    YOUR CODE HERE 👇
    """
    pass


def first_unique_hashmap(s: str) -> int:
    """
    Approach: Count frequencies, then find first with count 1.

    Hints:
    - Pass 1: Build frequency map {char: count}
    - Pass 2: Iterate string again, return first index where count == 1
    - Return -1 if no unique character exists
    - You can use collections.Counter

    Walk through:
        "leetcode"
        freq: {'l':1, 'e':3, 't':1, 'c':1, 'o':1, 'd':1}
        Scan: s[0]='l', freq['l']=1 → return 0

    YOUR CODE HERE 👇
    """
    pass


# ─── Test Cases ──────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Basic cases
    assert first_unique_hashmap("leetcode") == 0
    assert first_unique_hashmap("loveleetcode") == 2

    # 🔪 Edge cases
    assert first_unique_hashmap("aabb") == -1        # no unique
    assert first_unique_hashmap("") == -1             # empty string
    assert first_unique_hashmap("a") == 0             # single char
    assert first_unique_hashmap("aadadaad") == -1     # all repeated

    print("✅ All tests passed!")
