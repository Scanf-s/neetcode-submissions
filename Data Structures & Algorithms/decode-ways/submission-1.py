class Solution:
    def numDecodings(self, s: str) -> int:
        dp: list[int] = [0 for _ in range(len(s) + 1)]
        dp[0] = 1 if s[0] != '0' else 0
        dp[1] = 1 if s[0] != '0' else 0
        for idx in range(2, len(s) + 1):
            if s[idx - 1] != '0':
                dp[idx] += dp[idx - 1]
            
            iftwo: str = s[idx - 2:idx]
            if iftwo[0] != '0' and 0 < int(s[idx-2:idx]) <= 26:
                dp[idx] += dp[idx - 2]
        return dp[-1]
