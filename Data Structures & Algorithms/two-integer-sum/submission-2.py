from collections import defaultdict
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen: set = set()
        for num in nums:
            seen.add(num)
        
        idx_record = defaultdict(list[int])
        for idx in range(len(nums)):
            idx_record[nums[idx]].append(idx)

        print(idx_record)
        for idx in range(len(nums)):
            if target - nums[idx] in seen and idx_record[target - nums[idx]][-1] != idx:
                idx2: int = idx_record[target - nums[idx]][-1]
                return [idx, idx2] if idx2 > idx else [idx2, idx]

        return [-1, -1]
