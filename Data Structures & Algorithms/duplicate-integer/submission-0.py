from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_dict: Counter = Counter(nums)
        for cnt in nums_dict.values():
            if cnt >= 2:
                return True
        return False
        