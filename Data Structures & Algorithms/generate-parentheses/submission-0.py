class Solution:
    def recursive(self, opened: int, closed: int, n: int, cur: list[str], ans: list[str]) -> None:
        if opened + closed == 2 * n:
            ans.append(''.join(ch for ch in cur))
            return

        for ch in ['(', ')']:
            cur.append(ch)
            if opened < n and ch == '(':
                self.recursive(opened + 1, closed, n, cur, ans)
            elif opened > closed and closed < n and ch == ')':
                self.recursive(opened, closed + 1, n, cur, ans)
            cur.pop()

    def generateParenthesis(self, n: int) -> list[str]:
        ans: list[str] = []
        self.recursive(1, 0, n, ['('], ans)
        return ans
