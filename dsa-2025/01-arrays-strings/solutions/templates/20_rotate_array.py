"""
╔══════════════════════════════════════════════════════════════╗
║  Problem 20: Rotate Array                                    ║
╚══════════════════════════════════════════════════════════════╝

Difficulty: Medium
Pattern:    🔧 In-Place (reversal trick)
LeetCode:   https://leetcode.com/problems/rotate-array/

Key Insight: Three reversals — reverse all, reverse first k, reverse rest.
             This rotates in-place with O(1) space.
Time:  O(n)
Space: O(n) → O(1)  (extra array → reversal trick)

💡 Interview Tip: Know all three approaches. The reversal trick is elegant
   and uses O(1) space. The interviewer will likely ask you to optimize
   from O(n) space to O(1).

🧠 Pattern Recognition: "Rotate/shift in-place" = reversal trick.
   Works for both arrays and parts of linked lists.
"""

from typing import List


def rotate_extra_space(nums: List[int], k: int) -> None:
    """
    Approach: Use extra array.

    Hints:
    - k = k % len(nums)  — handle k > length
    - New position of nums[i] = (i + k) % n
    - Build new array, then copy back to nums in-place
    - Time: O(n), Space: O(n)

    YOUR CODE HERE 👇
    """
    pass


def rotate(nums: List[int], k: int) -> None:
    """
    Approach: Three reversals — O(1) space!

    Hints:
    - k = k % len(nums)  — handle k > length (e.g., k=10, n=7 → same as k=3)
    - Write a helper: def reverse(arr, start, end):
        while start < end: swap arr[start] and arr[end], move inward
    - Step 1: Reverse entire array:    reverse(nums, 0, n-1)
    - Step 2: Reverse first k elements: reverse(nums, 0, k-1)
    - Step 3: Reverse remaining n-k:   reverse(nums, k, n-1)

    Walk through:
        [1,2,3,4,5,6,7], k=3
        Step 1: reverse all →    [7,6,5,4,3,2,1]
        Step 2: reverse [0:3] → [5,6,7,4,3,2,1]
        Step 3: reverse [3:7] → [5,6,7,1,2,3,4] ✓

    WHY this works:
    - Original: [1,2,3,4 | 5,6,7]  (split at position n-k)
    - Want:     [5,6,7 | 1,2,3,4]  (swap the two halves)
    - Reverse all: both halves get reversed AND swapped positions
    - Reverse each half individually: un-reverses elements within each half

    YOUR CODE HERE 👇
    """
    pass


# ─── Test Cases ──────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Basic cases
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    rotate(nums1, 3)
    assert nums1 == [5, 6, 7, 1, 2, 3, 4]

    nums2 = [-1, -100, 3, 99]
    rotate(nums2, 2)
    assert nums2 == [3, 99, -1, -100]

    # 🔪 Edge cases
    nums3 = [1, 2, 3]
    rotate(nums3, 4)                   # k > length (same as k=1)
    assert nums3 == [3, 1, 2]

    nums4 = [1]
    rotate(nums4, 0)                   # k = 0
    assert nums4 == [1]

    nums5 = [1]
    rotate(nums5, 1)                   # single element, k=1
    assert nums5 == [1]

    nums6 = [1, 2]
    rotate(nums6, 1)                   # two elements
    assert nums6 == [2, 1]

    print("✅ All tests passed!")
