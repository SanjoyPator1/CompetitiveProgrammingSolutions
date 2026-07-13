"""
╔══════════════════════════════════════════════════════════════╗
║  Problem 8: Valid Palindrome                                 ║
╚══════════════════════════════════════════════════════════════╝

Difficulty: Easy
Pattern:    🔀 Two Pointers (converging from both ends)
LeetCode:   https://leetcode.com/problems/valid-palindrome/

Key Insight: Use two pointers from both ends, skip non-alphanumeric chars,
             compare case-insensitively.
Time:  O(n)
Space: O(1) — just two pointers

💡 Interview Tip: The tricky part is handling non-alphanumeric characters.
   Use `char.isalnum()` and `char.lower()`. Don't create a cleaned string
   — that's O(n) space.

🧠 Pattern Recognition: "Check symmetry" or "compare from both ends"
   = converging two pointers.
"""

from typing import List


def is_palindrome_clean(s: str) -> bool:
    """
    Approach: Clean string first, then check.

    Hints:
    - Filter out non-alphanumeric, convert to lowercase
    - Compare cleaned string with its reverse
    - Time: O(n), Space: O(n) — not optimal

    YOUR CODE HERE 👇
    """
    pass


def is_palindrome_two_pointers(s: str) -> bool:
    """
    Approach: Two pointers from both ends, skip non-alphanumeric.

    Hints:
    - left starts at 0, right starts at len-1
    - Skip non-alphanumeric: while not s[left].isalnum(): left += 1
    - Compare s[left].lower() == s[right].lower()
    - If mismatch → return False
    - If pointers meet → return True
    - Be careful with bounds checking!

    Walk through:
        "A man, a plan, a canal: Panama"
        left→'A' right→'a' → match (case insensitive)
        left→'m' right→'m' → match
        ...all match → True

    YOUR CODE HERE 👇
    """
    pass


# ─── Test Cases ──────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Basic cases
    assert is_palindrome_two_pointers("A man, a plan, a canal: Panama") == True
    assert is_palindrome_two_pointers("race a car") == False

    # 🔪 Edge cases
    assert is_palindrome_two_pointers("") == True     # empty is palindrome
    assert is_palindrome_two_pointers(" ") == True    # spaces only
    assert is_palindrome_two_pointers("a") == True    # single char
    assert is_palindrome_two_pointers(".,") == True   # only non-alnum
    assert is_palindrome_two_pointers("0P") == False  # mixed types

    print("✅ All tests passed!")
