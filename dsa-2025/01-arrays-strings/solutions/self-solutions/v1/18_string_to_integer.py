"""
╔══════════════════════════════════════════════════════════════╗
║  Problem 18: String to Integer (atoi)                        ║
╚══════════════════════════════════════════════════════════════╝

Difficulty: Medium
Pattern:    🔧 Linear Scan with state management
LeetCode:   https://leetcode.com/problems/string-to-integer-atoi/

Key Insight: Handle edge cases systematically: whitespace → sign →
             digits → overflow. Process in order.
Time:  O(n)
Space: O(1)

💡 Interview Tip: This is an edge-case-heavy problem. The algorithm is
   simple, but handling ALL edge cases correctly is the challenge. Process
   step by step: strip whitespace, handle sign, read digits, clamp to
   INT range.

🧠 Pattern Recognition: "Parse/convert with rules"
   = step-by-step state machine.
"""

from typing import List


def my_atoi(s: str) -> int:
    """
    Approach: Step-by-step parsing.

    Hints:
    - INT_MIN = -2**31  = -2147483648
    - INT_MAX = 2**31-1 = 2147483647
    - Step 1: Skip leading whitespace using an index pointer
    - Step 2: Check for sign (+/-), default to positive (+1)
      - Move index forward if sign present
    - Step 3: Read digits until non-digit or end of string
      - Build number: result = result * 10 + int(s[i])
      - Only process if s[i].isdigit()
    - Step 4: Apply sign: result = sign * result
    - Step 5: Clamp to 32-bit int range:
      - if result < INT_MIN → return INT_MIN
      - if result > INT_MAX → return INT_MAX

    Walk through:
        "   -42"
        Step 1: skip spaces → index=3, s[3]='-'
        Step 2: sign = -1, index=4
        Step 3: '4' → result=4, '2' → result=42
        Step 4: result = -1 * 42 = -42
        Step 5: -42 in range → return -42

    YOUR CODE HERE 👇
    """
    pass


# ─── Test Cases ──────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Basic cases
    assert my_atoi("42") == 42
    assert my_atoi("   -42") == -42
    assert my_atoi("4193 with words") == 4193

    # 🔪 Edge cases
    assert my_atoi("") == 0                    # empty
    assert my_atoi("   ") == 0                 # only spaces
    assert my_atoi("words and 987") == 0       # no leading digits
    assert my_atoi("+1") == 1                  # explicit plus
    assert my_atoi("+-12") == 0                # double sign → 0
    assert my_atoi("-91283472332") == -2147483648   # underflow → clamp
    assert my_atoi("91283472332") == 2147483647     # overflow → clamp
    assert my_atoi("   +0 123") == 0           # zero with trailing

    print("✅ All tests passed!")
