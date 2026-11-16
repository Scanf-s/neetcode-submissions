class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result: list[list[int]] = []
        seen: set = set()
        nums = sorted(nums)
        for base_idx in range(len(nums) - 2):
            base_num: int = nums[base_idx]
            start: int = base_idx + 1
            end: int = len(nums) - 1
            while start < end:
                cur_sum: int = base_num + nums[start] + nums[end]
                if cur_sum > 0:
                    end -= 1
                elif cur_sum < 0:
                    start += 1
                else:
                    candidate: list[int] = [nums[base_idx], nums[start], nums[end]]
                    if tuple(candidate) not in seen:
                        result.append(candidate)
                        seen.add(tuple(candidate))
                    start += 1
                    end -= 1
            
        return result