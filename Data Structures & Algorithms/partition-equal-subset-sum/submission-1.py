class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total: int = sum(nums)
        if total % 2 != 0:
            return False
        
        history: set = {0}
        for num in nums:
            temp_set: set = set()
            for sum_history in history:
                if sum_history + num <= total // 2:
                    temp_set.add(sum_history + num)
            history |= temp_set
        return True if total // 2 in history else False
