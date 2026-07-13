"""
╔══════════════════════════════════════════════════════════════╗
║  Problem 3: Two Sum                                          ║
╚══════════════════════════════════════════════════════════════╝

Difficulty: Easy
Pattern:    #️⃣ Hash Map (complement finding)
LeetCode:   https://leetcode.com/problems/two-sum/

Key Insight: For each number, check if (target - number) was seen before.
Time:  O(n²) →  O(n)   (brute → hash map)
Space: O(1)  →  O(n)   (brute → hash map)

💡 Interview Tip: This is THE most asked interview question. You MUST know
   both approaches cold. Interviewer will ask: "Can you do better than O(n²)?"
   
🧠 Pattern Recognition: Whenever you need to find a COMPLEMENT or PAIR,
   think Hash Map. "Have I seen the other half before?"
"""

from typing import List


def two_sum_brute(nums: List[int], target: int) -> List[int]:
    """
    Approach: Check every pair of numbers.
    
    Hints:
    - Two nested loops: for i, for j where j > i
    - Check if nums[i] + nums[j] == target
    - Time: O(n²), Space: O(1)
    
    YOUR CODE HERE 👇
    """
    for idx_a, val_a in enumerate(nums):
        for idx_b, val_b in enumerate(nums):
            if idx_a == idx_b:
                continue

            if val_a + val_b == target:
                print(f"found it brute : {val_a} + {val_b} for index : {idx_a}, {idx_b}")
                return [idx_a, idx_b]

    return [-1, -1]


def two_sum_optimized(nums: List[int], target: int) -> List[int]:
    """
    Approach: Hash Map — store seen numbers, look for complement.
    
    Hints:
    - Create a dict: {number: index}
    - For each num, calculate complement = target - num
    - If complement is in dict → found the pair!
    - If not → store current num in dict
    - Single pass through the array
    
    Walk through example:
        nums = [2, 7, 11, 15], target = 9
        
        i=0: num=2, complement=7, seen={}        → not found, store {2: 0}
        i=1: num=7, complement=2, seen={2: 0}    → FOUND! return [0, 1]
    
    YOUR CODE HERE 👇
    """
    seen = {}

    for idx, num in enumerate(nums):
        compliment = target-num # Tips: dont use abs
        print("compliment = ", compliment)

        if compliment in seen:
            print(f"found it optmised for num={num} and idx={idx}")
            print(f"    compliment={compliment} -> seen in idx = {seen[compliment]}")
            print(f"    will return {seen[compliment]} and {idx}")
            return [seen[compliment], idx]
        else:
            print(f"    will add to seen : seen[{num}]={idx} ")
            seen[num] = idx

    return [-1, -1]


# ─── Test Cases ──────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Basic cases
    assert two_sum_optimized([2, 7, 11, 15], target=9) == [0, 1]
    assert two_sum_optimized([3, 2, 4], target=6) == [1, 2]
    
    # 🔪 Edge cases
    assert two_sum_optimized([3, 3], target=6) == [0, 1]         # duplicates
    assert two_sum_optimized([0, 4, 3, 0], target=0) == [0, 3]   # zeros
    assert two_sum_optimized([-1, -2, -3, -4, -5], target=-8) == [2, 4]  # negatives

    # ✅ Also verify brute force gives same answers
    assert two_sum_brute([2, 7, 11, 15], target=9) == [0, 1]
    assert two_sum_brute([3, 2, 4], target=6) == [1, 2]

    print("✅ All tests passed!")
