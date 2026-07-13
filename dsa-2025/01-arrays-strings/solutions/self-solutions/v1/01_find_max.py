"""
╔══════════════════════════════════════════════════════════════╗
║  Problem 1: Find Maximum Element                             ║
╚══════════════════════════════════════════════════════════════╝

Difficulty: Easy
Pattern:    🔧 Linear Scan (fundamental traversal)
LeetCode:   N/A (warm-up problem)

Key Insight: Single pass through array, tracking the best seen so far.
Time:  O(n)  →  O(n)  (can't do better — must see every element)
Space: O(1)  →  O(1)
"""

from typing import List


def find_max_brute_force(arr: List[int]) -> int:
    """
    Approach: Compare every element.
    
    Hints:
    - Initialize max_val with the first element (NOT 0 — why?)
    - What if array has all negative numbers?
    - What if array has only one element?
    
    YOUR CODE HERE 👇
    """
    max_val = float("-inf")

    for val in arr:
        if val > max_val:
            max_val = val

    return max_val


def find_max_optimized(arr: List[int]) -> int:
    """
    For this problem, brute force IS the optimal solution.
    But try implementing it without using Python's built-in max().
    
    Think about: Can you also track the INDEX of the maximum?
    
    YOUR CODE HERE 👇
    """
    max_index , max_value = 0, arr[0]

    for idx, val in enumerate(arr):
        if val > max_value:
            max_index, max_value = idx, val

    print("Max value is :",max_value)
    print("Max index : ",max_index)

    return max_value


# ─── Test Cases ──────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Basic cases
    assert find_max_optimized([3, 1, 4, 1, 5, 9, 2, 6]) == 9
    assert find_max_optimized([1, 2, 3, 4, 5]) == 5
    assert find_max_optimized([5, 4, 3, 2, 1]) == 5

    # 🔪 Edge cases
    assert find_max_optimized([42]) == 42                    # single element
    assert find_max_optimized([-5, -3, -1, -8]) == -1        # all negatives
    assert find_max_optimized([7, 7, 7, 7]) == 7             # all same
    assert find_max_optimized([-1000000, 1000000]) == 1000000 # extremes

    print("✅ All tests passed!")
