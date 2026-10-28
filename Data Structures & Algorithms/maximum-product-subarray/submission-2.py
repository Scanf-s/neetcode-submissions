class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_arr: list[int] = [0 for _ in range(len(nums))]
        max_arr: list[int] = [0 for _ in range(len(nums))]
        if len(nums) == 1:
            return nums[0]
        min_arr[0] = nums[0]
        max_arr[0] = nums[0]
        for i in range(1, len(nums)):
            min_arr[i] = min(nums[i], min_arr[i - 1] * nums[i], max_arr[i - 1] * nums[i])
            max_arr[i] = max(nums[i], max_arr[i - 1] * nums[i], min_arr[i - 1] * nums[i])
        
        return max(max_arr)
