"""
╔══════════════════════════════════════════════════════════════╗
║  Problem 12: Longest Common Prefix                           ║
╚══════════════════════════════════════════════════════════════╝

Difficulty: Medium
Pattern:    🔧 Vertical Scanning (character-by-character comparison)
LeetCode:   https://leetcode.com/problems/longest-common-prefix/

Key Insight: Compare characters at the same position across all strings.
             Stop at first mismatch.
Time:  O(S) where S = sum of all characters in all strings
Space: O(1)

💡 Interview Tip: Multiple approaches exist (vertical scan, horizontal scan,
   divide & conquer, binary search). Vertical scan is simplest and sufficient.

🧠 Pattern Recognition: "Compare multiple sequences"
   = iterate position by position.
"""

from typing import List


def longest_common_prefix_brute(strs: List[str]) -> str:
    """
    Approach: Horizontal scan — compare first two, then result with third, etc.

    Hints:
    - Start with prefix = strs[0]
    - For each next string, shorten prefix until it matches
    - Use startswith() or manual character comparison
    - Time: O(S), Space: O(1)

    YOUR CODE HERE 👇
    """
    pass


def longest_common_prefix(strs: List[str]) -> str:
    """
    Approach: Vertical scan — check one character position at a time.

    Hints:
    - Edge case: empty list → return ""
    - For each position i (0, 1, 2, ...):
      - Get char at position i from first string
      - Check if ALL other strings have the same char at position i
      - If any string is too short or has different char → return prefix so far
    - Return strs[0][:i+1] built up char by char

    Walk through:
        ["flower", "flow", "flight"]
        pos 0: f,f,f → match
        pos 1: l,l,l → match
        pos 2: o,o,i → MISMATCH → return "fl"

    YOUR CODE HERE 👇
    """
    pass


# ─── Test Cases ──────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Basic cases
    assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"
    assert longest_common_prefix(["dog", "racecar", "car"]) == ""
    assert longest_common_prefix(["interspecies", "interstellar", "interstate"]) == "inters"

    # 🔪 Edge cases
    assert longest_common_prefix([""]) == ""              # single empty
    assert longest_common_prefix(["a"]) == "a"            # single string
    assert longest_common_prefix(["", "b"]) == ""         # one empty
    assert longest_common_prefix(["abc", "abc", "abc"]) == "abc"  # all same
    assert longest_common_prefix([]) == ""                # empty list

    print("✅ All tests passed!")
