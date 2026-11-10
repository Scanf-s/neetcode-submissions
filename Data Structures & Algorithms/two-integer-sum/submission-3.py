class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen: dict[int, int] = {}

        for idx, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], idx]

            seen[num] = idx

        return [-1, -1]
