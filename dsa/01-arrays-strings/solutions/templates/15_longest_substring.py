"""
╔══════════════════════════════════════════════════════════════╗
║  Problem 15: Longest Substring Without Repeating Characters  ║
╚══════════════════════════════════════════════════════════════╝

Difficulty: Medium
Pattern:    🪟 Sliding Window (variable size) + #️⃣ Hash Set/Map
LeetCode:   https://leetcode.com/problems/longest-substring-without-repeating-characters/

Key Insight: Expand window right, shrink from left when duplicate found.
             Track chars in window with a set or map.
Time:  O(n²) → O(n)  (brute → sliding window)
Space: O(min(n, alphabet_size))

💡 Interview Tip: This is THE classic sliding window problem. You must know
   this cold. The hash map variant (storing last index) is more optimal
   than hash set.

🧠 Pattern Recognition: "Longest/shortest substring with constraint"
   = Sliding Window. Always.
"""

from typing import List


def length_of_longest_substring_brute(s: str) -> int:
    """
    Approach: Check every substring.

    Hints:
    - For each start position, expand right until duplicate found
    - Track max length seen
    - Use a set to detect duplicates within current substring
    - Time: O(n²), Space: O(n)

    YOUR CODE HERE 👇
    """
    pass


def length_of_longest_substring(s: str) -> int:
    """
    Approach: Sliding window with hash set.

    Hints:
    - Maintain a window [left, right]
    - Use a set to track characters in current window
    - Expand right: add s[right] to set
    - If s[right] already in set → shrink from left until it's removed
    - Track max window size: right - left + 1

    ADVANCED variant (hash map storing last index):
    - Map each char to its last seen index
    - When duplicate found: left = max(left, last_index[char] + 1)
    - This avoids the inner while loop — true O(n)

    Walk through (set approach):
        "abcabcbb"
        [a]bcabcbb → window="a", len=1
        a[b]cabcbb → window="ab", len=2
        ab[c]abcbb → window="abc", len=3
        abc[a]bcbb → 'a' in set! remove from left until 'a' gone
                      → window="bca", len=3
        ...max = 3

    YOUR CODE HERE 👇
    """
    pass


# ─── Test Cases ──────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Basic cases
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    assert length_of_longest_substring("pwwkew") == 3

    # 🔪 Edge cases
    assert length_of_longest_substring("") == 0        # empty
    assert length_of_longest_substring(" ") == 1       # space character
    assert length_of_longest_substring("au") == 2      # two unique
    assert length_of_longest_substring("dvdf") == 3    # tricky: d appears, then v,d,f
    assert length_of_longest_substring("abcdefg") == 7 # all unique
    assert length_of_longest_substring("aab") == 2     # dup at start

    print("✅ All tests passed!")
