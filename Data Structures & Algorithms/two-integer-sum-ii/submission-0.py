class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start: int = 0
        end: int = len(numbers) - 1
        while start < end:
            cur_sum: int = numbers[start] + numbers[end]
            if cur_sum > target:
                end -= 1
            elif cur_sum < target:
                start += 1
            else:
                return [start + 1, end + 1]
        return [-1, -1]
