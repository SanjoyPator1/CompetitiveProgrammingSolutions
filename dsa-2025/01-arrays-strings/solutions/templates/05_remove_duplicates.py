"""
╔══════════════════════════════════════════════════════════════╗
║  Problem 5: Remove Duplicates from Sorted Array             ║
╚══════════════════════════════════════════════════════════════╝

Difficulty: Easy
Pattern:    🔀 Two Pointers (fast-slow / read-write)
LeetCode:   https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Key Insight: Use a "write" pointer to track where the next unique element goes,
             and a "read" pointer to scan through the array.
Time:  O(n)
Space: O(1) — in-place!

💡 Interview Tip: The array is SORTED — this is crucial. Because it's sorted,
   duplicates are always adjacent. This makes the two-pointer approach work.

🧠 Pattern Recognition: "In-place removal/compaction from sorted array"
   = fast-slow two pointers. The slow pointer marks the boundary of the result.
"""

from typing import List


def remove_duplicates(nums: List[int]) -> int:
    """
    Approach: Two pointers (write pointer + read pointer).
    
    Hints:
    - 'write' pointer: where to place the next unique element
    - 'read' pointer: scans through the array
    - Since sorted, compare nums[read] with nums[write-1] (or nums[read-1])
    - If different → it's a new unique element, write it
    - Return 'write' as the new length
    
    Walk through example:
        [1, 1, 2, 2, 3, 4, 4, 5]
         w
         r
        
        r=1: nums[1]=1 == nums[0]=1  → skip
        r=2: nums[2]=2 != nums[1]=1  → write! w=1, nums[1]=2
        r=3: nums[3]=2 == nums[2]=2  → skip
        r=4: nums[4]=3 != nums[3]=2  → write! w=2, nums[2]=3
        ...and so on
    
    YOUR CODE HERE 👇
    """
    pass


# ─── Test Cases ──────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Basic cases
    nums1 = [1, 1, 2, 2, 3, 4, 4, 5]
    k1 = remove_duplicates(nums1)
    assert k1 == 5
    assert nums1[:k1] == [1, 2, 3, 4, 5]

    nums2 = [1, 1, 2]
    k2 = remove_duplicates(nums2)
    assert k2 == 2
    assert nums2[:k2] == [1, 2]

    # 🔪 Edge cases
    nums3 = [1]
    k3 = remove_duplicates(nums3)
    assert k3 == 1                                   # single element
    assert nums3[:k3] == [1]

    nums4 = [1, 2, 3, 4, 5]
    k4 = remove_duplicates(nums4)
    assert k4 == 5                                   # no duplicates
    assert nums4[:k4] == [1, 2, 3, 4, 5]

    nums5 = [1, 1, 1, 1, 1]
    k5 = remove_duplicates(nums5)
    assert k5 == 1                                   # all same
    assert nums5[:k5] == [1]

    print("✅ All tests passed!")
