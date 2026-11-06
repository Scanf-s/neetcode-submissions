from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams: dict[str, list[str]] = defaultdict(list)
        for word in strs:
            normalized: str = ''.join(sorted(list(word)))
            anagrams[normalized].append(word)
        ans: list[list[str]] = []
        for key in anagrams.keys():
            ans.append(anagrams[key])
        return ans
