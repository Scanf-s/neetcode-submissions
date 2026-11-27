class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp: list[int] = [0 for _ in range(len(prices))]
        dp[0] = 0
        min_price: int = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            dp[i] = prices[i] - min_price
        
        return max(dp)
