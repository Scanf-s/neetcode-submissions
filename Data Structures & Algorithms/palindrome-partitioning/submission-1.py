class Solution:
    def is_palindrome(self, s: str) -> bool:
        start: int = 0
        end: int = len(s) - 1
        while start <= end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

    def recursion(self, idx: int, s: str, part: list[str], ans: list[list[str]]) -> None:
        if idx >= len(s):
            ans.append(part.copy())
            return

        for end in range(idx + 1, len(s) + 1):
            if end > len(s):
                break
            
            cur = s[idx:end]
            if self.is_palindrome(cur):
                part.append(cur)
                self.recursion(end, s, part, ans)
                part.pop()

    def partition(self, s: str) -> list[list[str]]:
        ans: list[list[str]] = []
        self.recursion(0, s, [], ans)
        return ans
