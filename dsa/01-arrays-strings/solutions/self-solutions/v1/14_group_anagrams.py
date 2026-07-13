"""
╔══════════════════════════════════════════════════════════════╗
║  Problem 14: Group Anagrams                                  ║
╚══════════════════════════════════════════════════════════════╝

Difficulty: Medium
Pattern:    #️⃣ Hash Map (grouping by key)
LeetCode:   https://leetcode.com/problems/group-anagrams/

Key Insight: Anagrams produce the same string when sorted. Use sorted
             string as hash key.
Time:  O(n × k log k) where k = max string length
Space: O(n × k)

💡 Interview Tip: Two key approaches — (1) sorted string as key,
   (2) character count tuple as key. Know both. The count tuple approach
   is O(n × k) time (no sorting).

🧠 Pattern Recognition: "Group items by shared property"
   = hash map where key = canonical form.
"""

from typing import List


def group_anagrams_sort(strs: List[str]) -> List[List[str]]:
    """
    Approach: Use sorted string as hash key.

    Hints:
    - from collections import defaultdict
    - groups = defaultdict(list)
    - For each word: key = tuple(sorted(word))
    - groups[key].append(word)
    - Return list(groups.values())

    Walk through:
        ["eat","tea","tan","ate","nat","bat"]
        sorted("eat") = "aet" → groups["aet"] = ["eat", "tea", "ate"]
        sorted("tan") = "ant" → groups["ant"] = ["tan", "nat"]
        sorted("bat") = "abt" → groups["abt"] = ["bat"]

    YOUR CODE HERE 👇
    """
    pass


def group_anagrams_count(strs: List[str]) -> List[List[str]]:
    """
    Approach: Use character count tuple as key (avoids sorting).

    Hints:
    - from collections import defaultdict
    - For each word, create a count array of 26 zeros
    - Count each character: count[ord(c) - ord('a')] += 1
    - Use tuple(count) as dictionary key
    - Time: O(n × k) — better than sorting approach!

    YOUR CODE HERE 👇
    """
    pass


# ─── Test Cases ──────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Basic case
    # Note: order within groups and order of groups doesn't matter
    # So test by converting to sets of frozensets
    result = group_anagrams_sort(["eat", "tea", "tan", "ate", "nat", "bat"])
    result_sets = set(frozenset(group) for group in result)
    expected = {frozenset(["bat"]), frozenset(["nat", "tan"]), frozenset(["ate", "eat", "tea"])}
    assert result_sets == expected

    # 🔪 Edge cases
    assert group_anagrams_sort([""]) == [[""]]    # empty string
    assert group_anagrams_sort(["a"]) == [["a"]]  # single char

    print("✅ All tests passed!")
