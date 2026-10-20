class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp: list[bool] = [False for _ in range(len(s) + 1)]
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(0, i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
        return dp[-1]