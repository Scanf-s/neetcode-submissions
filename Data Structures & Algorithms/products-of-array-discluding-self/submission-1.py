class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ans: list[int] = [0 for _ in range(len(nums))]
        zero_cnt: int = 0
        for num in nums:
            if num == 0:
                zero_cnt += 1
        
        if zero_cnt == 1:
            total_product: int = 1
            for num in nums:
                if num == 0:
                    continue
                total_product *= num
            
            for idx in range(len(nums)):
                if nums[idx] == 0:
                    ans[idx] = total_product
                else:
                    ans[idx] = 0
        elif zero_cnt >= 2:
            pass
        else:
            total_product: int = 1
            for num in nums:
                total_product *= num
            
            for idx in range(len(nums)):
                ans[idx] = total_product // nums[idx]
        
        return ans