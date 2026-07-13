"""
╔══════════════════════════════════════════════════════════════╗
║  Problem 17: Three Sum                                       ║
╚══════════════════════════════════════════════════════════════╝

Difficulty: Medium
Pattern:    🔀 Two Pointers (sort + fix one + two-pointer scan)
LeetCode:   https://leetcode.com/problems/3sum/

Key Insight: Sort array. Fix one element, then use Two Sum II (two
             pointers) on the remaining. Skip duplicates carefully.
Time:  O(n³) → O(n²)  (brute → sort + two pointers)
Space: O(1) extra (excluding output)

💡 Interview Tip: The duplicate-skipping logic is where most people mess
   up. After finding a triplet, skip all duplicate values for both left
   and right pointers. Also skip duplicate values for the fixed element.

🧠 Pattern Recognition: "K-Sum" problems reduce to "sort + fix one +
   Two Sum". 4Sum = fix one + 3Sum. It's recursive.
"""

from typing import List


def three_sum_brute(nums: List[int]) -> List[List[int]]:
    """
    Approach: Check all triplets.

    Hints:
    - Three nested loops: i, j, k where j > i and k > j
    - Check if nums[i] + nums[j] + nums[k] == 0
    - Use a set of sorted tuples to avoid duplicate triplets
    - Time: O(n³)

    YOUR CODE HERE 👇
    """
    pass


def three_sum(nums: List[int]) -> List[List[int]]:
    """
    Approach: Sort + Fix one + Two pointers.

    Hints:
    - Sort the array first
    - For each i from 0 to len-2 (fixed element):
      - Skip if i > 0 and nums[i] == nums[i-1]  (avoid duplicate triplets)
      - If nums[i] > 0: break  (sorted → can't sum to 0 with all positives)
      - Set left = i+1, right = len-1
      - Two pointer scan:
        - total = nums[i] + nums[left] + nums[right]
        - if total < 0 → left++
        - if total > 0 → right--
        - if total == 0 → add triplet, then skip duplicates:
            while left < right and nums[left] == nums[left+1]: left++
            while left < right and nums[right] == nums[right-1]: right--
            left++, right--

    Walk through:
        [-1, 0, 1, 2, -1, -4]
        Sorted: [-4, -1, -1, 0, 1, 2]

        i=0, nums[0]=-4: left=1, right=5
          -4 + (-1) + 2 = -3 < 0 → left++
          -4 + 0 + 2 = -2 < 0 → left++
          -4 + 1 + 2 = -1 < 0 → left++
          left >= right → done with i=0

        i=1, nums[1]=-1: left=2, right=5
          -1 + (-1) + 2 = 0 → FOUND [-1,-1,2], skip dups, left=3, right=4
          -1 + 0 + 1 = 0 → FOUND [-1,0,1], skip dups

        i=2, nums[2]=-1: skip (duplicate of nums[1])

    YOUR CODE HERE 👇
    """
    pass


# ─── Test Cases ──────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Basic case
    result = three_sum([-1, 0, 1, 2, -1, -4])
    result_sorted = sorted([sorted(x) for x in result])
    assert result_sorted == [[-1, -1, 2], [-1, 0, 1]]

    # 🔪 Edge cases
    assert three_sum([0, 1, 1]) == []           # no solution
    assert three_sum([0, 0, 0]) == [[0, 0, 0]]  # all zeros
    assert three_sum([]) == []                   # empty
    assert three_sum([0]) == []                  # too short

    result2 = three_sum([-1, 0, 1, 0])
    assert sorted([sorted(x) for x in result2]) == [[-1, 0, 1]]  # dups in result

    result3 = three_sum([-2, 0, 1, 1, 2])
    assert sorted([sorted(x) for x in result3]) == [[-2, 0, 2], [-2, 1, 1]]

    print("✅ All tests passed!")
