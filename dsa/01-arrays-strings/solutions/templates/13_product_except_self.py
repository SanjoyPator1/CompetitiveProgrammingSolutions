"""
╔══════════════════════════════════════════════════════════════╗
║  Problem 13: Product of Array Except Self                    ║
╚══════════════════════════════════════════════════════════════╝

Difficulty: Medium
Pattern:    📊 Prefix/Suffix (left-right product passes)
LeetCode:   https://leetcode.com/problems/product-of-array-except-self/

Key Insight: For each position, result = product of everything LEFT ×
             product of everything RIGHT. Build both in two passes.
Time:  O(n)
Space: O(1) extra (output array doesn't count)

💡 Interview Tip: The constraint "no division" is key. With division you'd
   just do total_product / nums[i], but that fails with zeros. The
   prefix/suffix approach handles zeros naturally.

🧠 Pattern Recognition: "Need aggregate of everything except current"
   = prefix + suffix passes.
"""

from typing import List


def product_except_self_brute(nums: List[int]) -> List[int]:
    """
    Approach: For each element, multiply all others.

    Hints:
    - For each i, loop through all j != i and multiply
    - Time: O(n²), Space: O(n)

    YOUR CODE HERE 👇
    """
    pass


def product_except_self(nums: List[int]) -> List[int]:
    """
    Approach: Two passes — left products then right products.

    Hints:
    - Create result array of 1s
    - LEFT PASS: result[i] = running product of all elements to the left
      - Maintain left_product, start at 1
      - result[i] = left_product, then left_product *= nums[i]
    - RIGHT PASS: multiply result[i] by running product from the right
      - Maintain right_product, start at 1
      - result[i] *= right_product, then right_product *= nums[i]
      - Iterate from right to left

    Walk through:
        nums = [1, 2, 3, 4]

        Left pass (left_product):
          result = [1, 1, 2, 6]    (each = product of everything before it)

        Right pass (right_product):
          result[3] *= 1 = 6       right_product = 4
          result[2] *= 4 = 8       right_product = 12
          result[1] *= 12 = 12     right_product = 24
          result[0] *= 24 = 24     right_product = 24

        result = [24, 12, 8, 6] ✓

    YOUR CODE HERE 👇
    """
    pass


# ─── Test Cases ──────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Basic cases
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]

    # 🔪 Edge cases
    assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]  # with zero
    assert product_except_self([1, 1]) == [1, 1]      # two elements
    assert product_except_self([2, 3]) == [3, 2]      # two elements
    assert product_except_self([0, 0]) == [0, 0]      # two zeros
    assert product_except_self([5]) == [1]             # single element

    print("✅ All tests passed!")
