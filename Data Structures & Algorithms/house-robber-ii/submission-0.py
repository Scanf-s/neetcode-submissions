class Solution:
    def rob(self, nums: List[int]) -> int:
        n: int = len(nums)
        from_start: list[int] = [0 for _ in range(n - 1)]
        from_second: list[int] = [0 for _ in range(n - 1)]
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        from_start[0] = nums[0]
        from_start[1] = max(nums[0], nums[1])
        for i in range(2, n - 1):
            from_start[i] = max(from_start[i - 1], nums[i] + from_start[i - 2])
        
        from_second[0] = nums[1]
        from_second[1] = max(nums[1], nums[2])
        for i in range(2, n - 1):
            from_second[i] = max(from_second[i - 1], nums[i + 1] + from_second[i - 2])
        return max(from_start[-1], from_second[-1])
        