"""
╔══════════════════════════════════════════════════════════════╗
║  Problem 19: Container With Most Water                       ║
╚══════════════════════════════════════════════════════════════╝

Difficulty: Medium
Pattern:    🔀 Two Pointers (greedy converging)
LeetCode:   https://leetcode.com/problems/container-with-most-water/

Key Insight: Start with widest container (left=0, right=end). Move the
             pointer with the SHORTER line inward — you can only improve
             by finding a taller line.
Time:  O(n²) → O(n)  (brute → two pointers)
Space: O(1)

💡 Interview Tip: The WHY behind moving the shorter pointer is the key
   insight. Moving the taller pointer can NEVER increase area (width
   decreases, height bounded by shorter side). This greedy argument is
   what interviewers want to hear.

🧠 Pattern Recognition: "Maximize area/value between two boundaries"
   = converging two pointers with greedy choice.
"""

from typing import List


def max_area_brute(height: List[int]) -> int:
    """
    Approach: Check every pair of lines.

    Hints:
    - For each pair (i, j) where j > i:
      area = min(height[i], height[j]) * (j - i)
    - Track maximum area seen
    - Time: O(n²)

    YOUR CODE HERE 👇
    """
    pass


def max_area(height: List[int]) -> int:
    """
    Approach: Two pointers — start wide, move shorter side inward.

    Hints:
    - left = 0, right = len(height) - 1
    - Loop while left < right:
      - current area = min(height[left], height[right]) * (right - left)
      - Update max area
      - If height[left] < height[right] → move left++ (left is shorter)
      - Else → move right-- (right is shorter or equal)

    WHY this works:
    - Width always decreases by 1 each step
    - Only way to increase area is to find taller height
    - Moving the taller pointer can't help (area still limited by shorter)
    - So always move the shorter pointer — greedy optimal choice

    Walk through:
        [1,8,6,2,5,4,8,3,7]
        l=0,r=8: area=min(1,7)*8=8,  move left (1<7)
        l=1,r=8: area=min(8,7)*7=49, move right (7<8)
        l=1,r=7: area=min(8,3)*6=18, move right (3<8)
        l=1,r=6: area=min(8,8)*5=40, move right (equal, pick either)
        ... max=49

    YOUR CODE HERE 👇
    """
    pass


# ─── Test Cases ──────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Basic cases
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49

    # 🔪 Edge cases
    assert max_area([1, 1]) == 1              # minimum case (two lines)
    assert max_area([4, 3, 2, 1, 4]) == 16   # first and last same height
    assert max_area([1, 2, 1]) == 2           # small array
    assert max_area([2, 3, 4, 5, 18, 17, 6]) == 17  # tall lines in middle

    print("✅ All tests passed!")
