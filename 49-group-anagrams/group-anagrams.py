class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_map = defaultdict(list)

        for item in strs:
            count = [0] * 26

            for c in item:
                i = ord(c) - ord("a")
                count[i] += 1

            anagram_map[tuple(count)].append(item)

        return list(anagram_map.values())