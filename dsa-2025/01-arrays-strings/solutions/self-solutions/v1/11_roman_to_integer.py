"""
╔══════════════════════════════════════════════════════════════╗
║  Problem 11: Roman to Integer                                ║
╚══════════════════════════════════════════════════════════════╝

Difficulty: Medium
Pattern:    #️⃣ Hash Map (lookup table) + Linear Scan
LeetCode:   https://leetcode.com/problems/roman-to-integer/

Key Insight: If a smaller value appears BEFORE a larger value, subtract it
             (e.g., IV = 4). Otherwise, add it.
Time:  O(n)
Space: O(1) — fixed-size lookup map (7 entries)

💡 Interview Tip: The subtraction rule is the only tricky part. Compare
   current char value with NEXT char value.

🧠 Pattern Recognition: "Convert using rules with context"
   = scan with lookahead.
"""

from typing import List


def roman_to_int(s: str) -> int:
    """
    Approach: Map + linear scan with lookahead.

    Hints:
    - Create map: {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    - Iterate through string
    - If current value < next value → SUBTRACT current (e.g., I before V = 4)
    - Otherwise → ADD current
    - Handle last character separately (no next to compare)

    Walk through:
        "MCMXCIV" = 1994
        M=1000 (M>C → add) → 1000
        C=100  (C<M → subtract) → 900
        M=1000 (M>X → add) → 1900
        X=10   (X<C → subtract) → 1890
        C=100  (C>I → add) → 1990
        I=1    (I<V → subtract) → 1989... wait
        V=5    (last → add) → 1994 ✓

    YOUR CODE HERE 👇
    """
    pass


# ─── Test Cases ──────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Basic cases
    assert roman_to_int("III") == 3
    assert roman_to_int("LVIII") == 58
    assert roman_to_int("MCMXCIV") == 1994

    # 🔪 Edge cases — subtraction rules
    assert roman_to_int("IV") == 4         # subtraction case
    assert roman_to_int("IX") == 9         # subtraction case
    assert roman_to_int("XL") == 40        # subtraction case
    assert roman_to_int("XC") == 90        # subtraction case
    assert roman_to_int("CD") == 400       # subtraction case
    assert roman_to_int("CM") == 900       # subtraction case
    assert roman_to_int("I") == 1          # single char
    assert roman_to_int("MMMCMXCIX") == 3999  # max valid roman

    print("✅ All tests passed!")
