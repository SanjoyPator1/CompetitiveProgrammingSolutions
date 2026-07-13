"""
╔══════════════════════════════════════════════════════════════╗
║  Problem 7: Move Zeros                                       ║
╚══════════════════════════════════════════════════════════════╝

Difficulty: Easy
Pattern:    🔀 Two Pointers (fast-slow / read-write) + 🔧 In-Place
LeetCode:   https://leetcode.com/problems/move-zeroes/

Key Insight: Use a write pointer to place non-zero elements at the front,
             then fill rest with zeros.
Time:  O(n)
Space: O(1) — in-place

💡 Interview Tip: This is the exact same pattern as Remove Duplicates
   (Problem 5). If you solved that, this is free. Interviewers look for
   you to recognize this.

🧠 Pattern Recognition: "Move/remove elements in-place" = fast-slow two
   pointers. The write pointer always trails behind or stays with the
   read pointer.
"""

from typing import List


def move_zeros(nums: List[int]) -> None:
    """
    Approach: Write pointer for non-zeros, then fill remaining with 0.

    Hints:
    - 'write' pointer starts at 0
    - Scan with 'read' pointer: if nums[read] != 0, copy to write position
    - After scan, fill positions from 'write' to end with 0
    - Modify array in-place, return None

    Walk through:
        [0, 1, 0, 3, 12]
        read=0: 0 → skip
        read=1: 1 → write to pos 0, write=1
        read=2: 0 → skip
        read=3: 3 → write to pos 1, write=2
        read=4: 12 → write to pos 2, write=3
        Fill [3:] with 0 → [1, 3, 12, 0, 0]

    YOUR CODE HERE 👇
    """
    pass


# ─── Test Cases ──────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Basic cases
    nums1 = [0, 1, 0, 3, 12]
    move_zeros(nums1)
    assert nums1 == [1, 3, 12, 0, 0]

    # 🔪 Edge cases
    nums2 = [0]
    move_zeros(nums2)
    assert nums2 == [0]               # single zero

    nums3 = [1, 2, 3]
    move_zeros(nums3)
    assert nums3 == [1, 2, 3]         # no zeros

    nums4 = [0, 0, 0, 0]
    move_zeros(nums4)
    assert nums4 == [0, 0, 0, 0]      # all zeros

    nums5 = [1]
    move_zeros(nums5)
    assert nums5 == [1]               # single non-zero

    nums6 = [0, 0, 1]
    move_zeros(nums6)
    assert nums6 == [1, 0, 0]         # zeros at start

    print("✅ All tests passed!")
