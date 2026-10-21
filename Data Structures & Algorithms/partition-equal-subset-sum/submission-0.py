class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total: int = sum(nums)
        if total % 2 != 0:
            return False
        
        history: set = {0}
        dp: list[int] = [False for _ in range((total // 2) + 1)]
        for num in nums:
            temp_set: set = set()
            for sum_history in history:
                if sum_history + num <= total // 2:
                    temp_set.add(sum_history + num)
                    dp[sum_history + num] = True
            history = history | temp_set
        return dp[-1]
