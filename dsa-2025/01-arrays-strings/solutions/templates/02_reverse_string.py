"""
╔══════════════════════════════════════════════════════════════╗
║  Problem 2: Reverse String                                   ║
╚══════════════════════════════════════════════════════════════╝

Difficulty: Easy
Pattern:    🔀 Two Pointers (converging from both ends)
LeetCode:   https://leetcode.com/problems/reverse-string/

Key Insight: Swap characters from outside-in using two pointers.
Time:  O(n)  →  O(n)
Space: O(n)  →  O(1) (in-place with list)

💡 Interview Tip: In Python, strings are immutable. Convert to list first
   for in-place reversal. Interviewers WILL ask about this.
"""

from typing import List


def reverse_string_brute(s: str) -> str:
    """
    Approach: Build new string by reading backwards.
    
    Hints:
    - You can use slicing s[::-1] but DON'T — show the algorithm
    - Build a new list and join at the end
    
    YOUR CODE HERE 👇
    """
    pass


def reverse_string_two_pointers(s: List[str]) -> None:
    """
    Approach: Two pointers — swap from both ends, move inward.
    
    This is the in-place version (modifies list directly, returns None).
    This is what LeetCode expects.
    
    Hints:
    - left pointer starts at 0, right pointer starts at len-1
    - Swap s[left] and s[right], then move both inward
    - Stop when left >= right
    
    YOUR CODE HERE 👇
    """
    pass


# ─── Test Cases ──────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Test brute force (returns new string)
    assert reverse_string_brute("hello") == "olleh"
    assert reverse_string_brute("Python") == "nohtyP"
    
    # ✅ Test two pointers (modifies in-place)
    chars1 = list("hello")
    reverse_string_two_pointers(chars1)
    assert chars1 == list("olleh")
    
    chars2 = list("Hannah")
    reverse_string_two_pointers(chars2)
    assert chars2 == list("hannaH")

    # 🔪 Edge cases
    assert reverse_string_brute("") == ""             # empty string
    assert reverse_string_brute("a") == "a"           # single char
    assert reverse_string_brute("ab") == "ba"         # two chars
    assert reverse_string_brute("aaa") == "aaa"       # all same

    chars3 = list("a")
    reverse_string_two_pointers(chars3)
    assert chars3 == list("a")                         # single char in-place

    print("✅ All tests passed!")
