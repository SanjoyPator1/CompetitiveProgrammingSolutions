"""
╔══════════════════════════════════════════════════════════════╗
║  Problem 9: Merge Sorted Arrays                              ║
╚══════════════════════════════════════════════════════════════╝

Difficulty: Easy
Pattern:    🔀 Two Pointers (three pointers, merge from the end)
LeetCode:   https://leetcode.com/problems/merge-sorted-array/

Key Insight: Start merging from the END of nums1 (where there's empty
             space). Compare largest elements first.
Time:  O(m + n)
Space: O(1) — in-place

💡 Interview Tip: The key trick is merging BACKWARDS. If you merge
   forward, you'll overwrite elements you haven't processed yet.
   This is a classic insight.

🧠 Pattern Recognition: "Merge two sorted sequences in-place"
   = three pointers from the end.
"""

from typing import List


def merge_brute(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Approach: Copy nums2 into nums1, then sort.

    Hints:
    - Place nums2 elements at positions m, m+1, ... m+n-1
    - Sort the entire array
    - Time: O((m+n) log(m+n)), Space: O(1)

    YOUR CODE HERE 👇
    """
    pass


def merge_optimized(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Approach: Three pointers, merge from the end.

    Hints:
    - p1 = m - 1 (last real element in nums1)
    - p2 = n - 1 (last element in nums2)
    - write = m + n - 1 (last position in nums1)
    - Compare nums1[p1] vs nums2[p2], place larger at write position
    - Move the used pointer and write pointer backward
    - If p1 runs out, copy remaining nums2 elements
    - (If p2 runs out, nums1 elements are already in place!)

    Walk through:
        nums1 = [1,2,3,0,0,0], m=3, nums2 = [2,5,6], n=3
        write=5: compare 3 vs 6 → place 6 at [5]
        write=4: compare 3 vs 5 → place 5 at [4]
        write=3: compare 3 vs 2 → place 3 at [3]
        write=2: compare 2 vs 2 → place 2 at [2]
        write=1: p1=0, compare 1 vs 2 → place 2 at [1]
        p2 done → result [1,2,2,3,5,6]

    YOUR CODE HERE 👇
    """
    pass


# ─── Test Cases ──────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Basic cases
    nums1 = [1, 2, 3, 0, 0, 0]
    merge_optimized(nums1, 3, [2, 5, 6], 3)
    assert nums1 == [1, 2, 2, 3, 5, 6]

    # 🔪 Edge cases
    nums2 = [1]
    merge_optimized(nums2, 1, [], 0)
    assert nums2 == [1]                   # nothing to merge

    nums3 = [0]
    merge_optimized(nums3, 0, [1], 1)
    assert nums3 == [1]                   # nums1 is empty

    nums4 = [4, 5, 6, 0, 0, 0]
    merge_optimized(nums4, 3, [1, 2, 3], 3)
    assert nums4 == [1, 2, 3, 4, 5, 6]   # nums2 all smaller

    nums5 = [1, 2, 3, 0, 0, 0]
    merge_optimized(nums5, 3, [4, 5, 6], 3)
    assert nums5 == [1, 2, 3, 4, 5, 6]   # nums2 all larger

    print("✅ All tests passed!")
