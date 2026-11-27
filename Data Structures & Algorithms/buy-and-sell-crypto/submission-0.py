class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp: list[int] = [0 for _ in range(len(prices))]
        dp[0] = 0
        for i in range(1, len(prices)):
            candidates: list[int] = []
            for j in range(i):
                if prices[j] < prices[i]:
                    candidates.append(prices[j])

            if candidates:
                dp[i] = prices[i] - min(candidates)
        
        return max(dp)
