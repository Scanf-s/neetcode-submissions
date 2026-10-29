class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n: int = len(cost)
        if n == 2:
            return min(cost[0], cost[1])

        dp: list[int] = [0 for _ in range(n)]
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, n):
            dp[i] = min(dp[i - 2], dp[i - 1]) + cost[i]
        return min(dp[-1], dp[-2])
