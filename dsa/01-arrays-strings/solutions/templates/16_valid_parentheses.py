"""
╔══════════════════════════════════════════════════════════════╗
║  Problem 16: Valid Parentheses                               ║
╚══════════════════════════════════════════════════════════════╝

Difficulty: Medium
Pattern:    📚 Stack (matching pairs)
LeetCode:   https://leetcode.com/problems/valid-parentheses/

Key Insight: Push opening brackets onto stack, pop when matching closing
             bracket found. Stack must be empty at end.
Time:  O(n)
Space: O(n)

💡 Interview Tip: This is technically a Stack problem, not purely arrays.
   But it's a MUST-KNOW. The hash map for matching pairs makes the code
   clean and handles all bracket types elegantly.

🧠 Pattern Recognition: "Matching/nesting" = Stack. Any time you need to
   match opening/closing or handle nesting, think Stack.
"""

from typing import List


def is_valid(s: str) -> bool:
    """
    Approach: Stack with hash map for matching.

    Hints:
    - Create matching map: {')':'(', '}':'{', ']':'['}
    - Iterate through string:
      - If opening bracket ( [ { → push to stack
      - If closing bracket ) ] } → check if top of stack matches
        - If stack is empty OR top doesn't match → return False
        - If matches → pop
    - At end, return True only if stack is empty (all brackets closed)
    - Edge: empty string → True

    Walk through:
        "([{}])"
        '(' → push → stack: ['(']
        '[' → push → stack: ['(', '[']
        '{' → push → stack: ['(', '[', '{']
        '}' → matches '{' → pop → stack: ['(', '[']
        ']' → matches '[' → pop → stack: ['(']
        ')' → matches '(' → pop → stack: []
        Stack empty → True ✓

    YOUR CODE HERE 👇
    """
    pass


# ─── Test Cases ──────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Basic cases
    assert is_valid("()") == True
    assert is_valid("()[]{}") == True
    assert is_valid("(]") == False
    assert is_valid("([)]") == False
    assert is_valid("{[]}") == True

    # 🔪 Edge cases
    assert is_valid("") == True           # empty string
    assert is_valid("(") == False         # unclosed bracket
    assert is_valid(")") == False         # no opener
    assert is_valid("(((())))") == True   # deeply nested
    assert is_valid("({[)]}") == False    # interleaved wrong

    print("✅ All tests passed!")
