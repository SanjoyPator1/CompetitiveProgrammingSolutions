"""
╔══════════════════════════════════════════════════════════════╗
║  Problem 4: Valid Anagram                                    ║
╚══════════════════════════════════════════════════════════════╝

Difficulty: Easy
Pattern:    #️⃣ Hash Map (frequency counting)
LeetCode:   https://leetcode.com/problems/valid-anagram/

Key Insight: Two strings are anagrams if they have the same character frequencies.
Time:  O(n log n) →  O(n)   (sorting → hash map)
Space: O(n)       →  O(1)   (sorted copies → 26-char counter)

💡 Interview Tip: Follow-up question — "What if the input contains Unicode?"
   Answer: Use a hash map instead of fixed-size array.
   
🧠 Pattern Recognition: Whenever you need to compare FREQUENCIES or COUNTS
   of elements, reach for Counter / frequency map.
"""

from typing import List


def is_anagram_sort(s: str, t: str) -> bool:
    """
    Approach: Sort both strings and compare.
    
    Hints:
    - If sorted versions are equal → anagram
    - Time: O(n log n), Space: O(n)
    - Simple but not optimal
    
    YOUR CODE HERE 👇
    """
    pass


def is_anagram_hashmap(s: str, t: str) -> bool:
    """
    Approach: Count character frequencies and compare.
    
    Hints:
    - Quick check: if len(s) != len(t), return False immediately
    - Count chars in s (increment), count chars in t (decrement)
    - If all counts are 0 → anagram
    - You can use collections.Counter or build your own dict
    
    YOUR CODE HERE 👇
    """
    pass


# ─── Test Cases ──────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Basic cases
    assert is_anagram_hashmap("listen", "silent") == True
    assert is_anagram_hashmap("anagram", "nagaram") == True
    assert is_anagram_hashmap("rat", "car") == False

    # 🔪 Edge cases
    assert is_anagram_hashmap("", "") == True              # both empty
    assert is_anagram_hashmap("a", "a") == True            # single char
    assert is_anagram_hashmap("a", "b") == False           # single char diff
    assert is_anagram_hashmap("ab", "a") == False          # different lengths
    assert is_anagram_hashmap("aabb", "abab") == True      # repeated chars
    assert is_anagram_hashmap("aacc", "ccac") == False     # same chars, diff freq

    # ✅ Verify sorting approach too
    assert is_anagram_sort("listen", "silent") == True
    assert is_anagram_sort("rat", "car") == False

    print("✅ All tests passed!")
