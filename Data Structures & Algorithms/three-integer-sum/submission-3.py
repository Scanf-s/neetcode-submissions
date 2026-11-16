class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result: list[list[int]] = []
        nums = sorted(nums)
        for base_idx in range(len(nums) - 2):
            base_num: int = nums[base_idx]
            if base_idx > 0 and base_num == nums[base_idx - 1]:
                continue
            if base_num > 0:
                break
            
            start: int = base_idx + 1
            end: int = len(nums) - 1
            while start < end:
                cur_sum: int = base_num + nums[start] + nums[end]
                if cur_sum > 0:
                    end -= 1
                elif cur_sum < 0:
                    start += 1
                else:
                    result.append([nums[base_idx], nums[start], nums[end]])

                    start += 1
                    end -= 1
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
                    while start < end and nums[end] == nums[end + 1]:
                        end -= 1
            
        return result