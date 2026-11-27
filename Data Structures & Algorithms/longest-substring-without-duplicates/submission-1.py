class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start: int = 0
        end: int = 0
        seen: set = set()
        max_seq: int = 0
        while end < len(s):
            if s[end] not in seen:
                seen.add(s[end])
                end += 1
            else:
                while s[end] in seen:
                    seen.remove(s[start])
                    start += 1
                seen.add(s[end])
                end += 1
            max_seq = max(max_seq, end - start)
        return max_seq