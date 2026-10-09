class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_map = {}

        for item in strs:
            item_sorted = str(sorted(item.lower()))

            anagram_map.setdefault(item_sorted, []).append(item)

        return list(anagram_map.values())