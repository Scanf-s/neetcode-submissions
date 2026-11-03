class Solution:
    def recursive(self, opened: int, closed: int, n: int, cur: list[str], ans: list[str]) -> None:
        if opened + closed == 2 * n:
            ans.append(''.join(ch for ch in cur))
            return

        if opened < n:
            cur.append('(')
            self.recursive(opened + 1, closed, n, cur, ans)
            cur.pop()

        if closed < opened:
            cur.append(')')
            self.recursive(opened, closed + 1, n, cur, ans)
            cur.pop()

    def generateParenthesis(self, n: int) -> list[str]:
        ans: list[str] = []
        self.recursive(1, 0, n, ['('], ans)
        return ans
