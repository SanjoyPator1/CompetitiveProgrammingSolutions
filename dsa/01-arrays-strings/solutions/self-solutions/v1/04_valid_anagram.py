"""
╔══════════════════════════════════════════════════════════════╗
║  Problem 4: Valid Anagram                                    ║
╚══════════════════════════════════════════════════════════════╝

Difficulty: Easy
Pattern:    #️⃣ Hash Map (frequency counting)
LeetCode:   https://leetcode.com/problems/valid-anagram/

Key Insight: Two strings are anagrams if they have the same character frequencies.
Time:  O(n log n) →  O(n)   (sorting → hash map)
Space: O(n)       →  O(1)   (sorted copies → 26-char counter)

💡 Interview Tip: Follow-up question — "What if the input contains Unicode?"
   Answer: Use a hash map instead of fixed-size array.
   
🧠 Pattern Recognition: Whenever you need to compare FREQUENCIES or COUNTS
   of elements, reach for Counter / frequency map.
"""

from typing import List
from collections import defaultdict


def is_anagram_sort(s: str, t: str) -> bool:
    """
    Approach: Sort both strings and compare.
    
    Hints:
    - If sorted versions are equal → anagram
    - Time: O(n log n), Space: O(n)
    - Simple but not optimal
    
    YOUR CODE HERE 👇
    """
    # TIPS: in python strings are immutable - so no .sort() but we can use python's built-in sorted() function
    # When you pass a string to sorted(), it breaks the string into individual characters, sorts them alphabetically, and returns a list of those sorted characters.
    
    # print("sorted s is : ",sorted(s))
    # print("sorted t is : ",sorted(t))

    return sorted(s) == sorted(t)


def is_anagram_hashmap(s: str, t: str) -> bool:
    """
    Approach: Count character frequencies and compare.
    
    Hints:
    - Quick check: if len(s) != len(t), return False immediately
    - Count chars in s (increment), count chars in t (decrement)
    - If all counts are 0 → anagram
    - You can use collections.Counter or build your own dict
    
    YOUR CODE HERE 👇
    """
    # TIP: quick check the length should be equal if anagram
    if len(s) != len(t):
        return False

    # TIP: maintain dic for freq counter for both the strings
    freq_map_s = {}
    freq_map_t = {}

    # create freq map for s
    for val in s:
        if val in freq_map_s:
            freq_map_s[val] += 1
        else:
            freq_map_s[val] = 1

    # print("freq_map_s : ",freq_map_s)

    # create freq map for t
    for val in t:
        if val in freq_map_t:
            freq_map_t[val] += 1
        else:
            freq_map_t[val] = 1

    # print("freq_map_t : ",freq_map_t)

    return freq_map_s == freq_map_t

# pythonic way and also more optimized
def is_anagram_hashmap(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    # maintain one dict and also use default dict to have it as 0 and also decrement when same char found in string t and check at the end if each value is 0 - this way one dict wins - saves space
    freq_map_s = defaultdict(int)   # missing keys automatically start at 0

    for val in s:
        freq_map_s[val] += 1    # if key is not present it will have 0 by default and plus 1
        # if the above was not defaultdict we could use something like this - more pythonic
        # freq_map_s[val] = freq_map_s.get(val, 0) + 1

    # now decrement each char frequency
    for val in t:
        # if the val is not found in s then its not anagram - edge case
        if val not in freq_map_s:
            return False
        else:
            freq_map_s[val] -= 1

    # check if all the char in freq_map_s is 0
    for key, val in freq_map_s.items():
        # print("val is ",val)
        if val !=0:
            return False
    
    return True

# ─── Test Cases ──────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Basic cases
    assert is_anagram_hashmap("listen", "silent") == True
    assert is_anagram_hashmap("anagram", "nagaram") == True
    assert is_anagram_hashmap("rat", "car") == False

    # 🔪 Edge cases
    assert is_anagram_hashmap("", "") == True              # both empty
    assert is_anagram_hashmap("a", "a") == True            # single char
    assert is_anagram_hashmap("a", "b") == False           # single char diff
    assert is_anagram_hashmap("ab", "a") == False          # different lengths
    assert is_anagram_hashmap("aabb", "abab") == True      # repeated chars
    assert is_anagram_hashmap("aacc", "ccac") == False     # same chars, diff freq

    # ✅ Verify sorting approach too
    assert is_anagram_sort("listen", "silent") == True
    assert is_anagram_hashmap("rat", "car") == False

    print("✅ All tests passed!")


# TIPS: This question is a good start for learning dict, default dic, get in dict with 0 and increment freq counter