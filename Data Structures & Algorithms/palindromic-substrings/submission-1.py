class Solution:

    def countSubstrings(self, s: str) -> int:
        ans: int = 0
        for i in range(len(s)):
            # odd
            start: int = i
            end: int = i
            while start >= 0 and end < len(s) and s[start] == s[end]:
                ans += 1
                start -= 1
                end += 1

            # even
            start = i
            end = i + 1
            while start >= 0 and end < len(s) and s[start] == s[end]:
                ans += 1
                start -= 1
                end += 1
        return ans