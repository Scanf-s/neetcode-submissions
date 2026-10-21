class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp: list[int] = [-1 for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(1, amount + 1):
            candidates: list[int] = []
            for coin in coins:
                if coin <= i and dp[i - coin] != -1:
                    candidates.append(dp[i - coin])
            if candidates:
                dp[i] = min(candidates) + 1
        print(dp)
        return dp[-1]