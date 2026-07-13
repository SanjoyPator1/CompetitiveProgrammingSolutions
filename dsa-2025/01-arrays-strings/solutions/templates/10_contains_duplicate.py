"""
╔══════════════════════════════════════════════════════════════╗
║  Problem 10: Contains Duplicate                              ║
╚══════════════════════════════════════════════════════════════╝

Difficulty: Easy
Pattern:    #️⃣ Hash Set (existence check)
LeetCode:   https://leetcode.com/problems/contains-duplicate/

Key Insight: A set gives O(1) lookup — add elements, if already in set
             → duplicate found.
Time:  O(n² or n log n) → O(n)  (brute/sort → hash set)
Space: O(1)              → O(n)  (brute → hash set)

💡 Interview Tip: Three approaches exist. Know trade-offs:
   brute O(n²)/O(1), sort O(n log n)/O(1), hash set O(n)/O(n).

🧠 Pattern Recognition: "Does X exist in collection?" = Hash Set.
   Fastest existence check.
"""

from typing import List


def contains_duplicate_brute(nums: List[int]) -> bool:
    """
    Approach: Check every pair.

    Hints:
    - Two nested loops, compare all pairs
    - Time: O(n²), Space: O(1)

    YOUR CODE HERE 👇
    """
    pass


def contains_duplicate_sort(nums: List[int]) -> bool:
    """
    Approach: Sort, then check adjacent elements.

    Hints:
    - Sort the array
    - If any nums[i] == nums[i+1] → duplicate
    - Time: O(n log n), Space: O(1) if in-place sort

    YOUR CODE HERE 👇
    """
    pass


def contains_duplicate_set(nums: List[int]) -> bool:
    """
    Approach: Use a hash set.

    Hints:
    - Iterate through array
    - If num already in set → return True
    - Otherwise add to set
    - Time: O(n), Space: O(n)

    Alternative one-liner (know this but explain the above in interview):
        return len(nums) != len(set(nums))

    YOUR CODE HERE 👇
    """
    pass


# ─── Test Cases ──────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Basic cases
    assert contains_duplicate_set([1, 2, 3, 1]) == True
    assert contains_duplicate_set([1, 2, 3, 4]) == False
    assert contains_duplicate_set([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True

    # 🔪 Edge cases
    assert contains_duplicate_set([]) == False        # empty
    assert contains_duplicate_set([1]) == False       # single element
    assert contains_duplicate_set([1, 1]) == True     # two same
    assert contains_duplicate_set([1, 2]) == False    # two different

    print("✅ All tests passed!")
