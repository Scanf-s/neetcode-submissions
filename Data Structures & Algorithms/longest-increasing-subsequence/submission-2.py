class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp: list[int] = [0 for _ in range(len(nums))]
        dp[0] = 1
        for i in range(1, len(nums)):
            j: int = i - 1
            candidates: list[int] = []
            while j >= 0:
                if nums[j] < nums[i]:
                    candidates.append(dp[j])
                j -= 1
            if not candidates:
                dp[i] = 1
            else:
                dp[i] = max(candidates) + 1

        return max(dp)