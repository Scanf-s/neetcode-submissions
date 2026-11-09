class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        seen: set = set()
        min_num: int = min(nums)
        max_num: int = max(nums)
        max_lcs: int = 0
        for num in nums:
            if num in seen:
                continue
            
            cur_lcs: int = 0
            cur_num: int = num
            seen.add(num)

            while cur_num >= min_num and cur_num in seen:
                cur_lcs += 1
                cur_num -= 1
            
            cur_num = num + 1
            while cur_num <= max_num and cur_num in seen:
                cur_lcs += 1
                cur_num += 1

            max_lcs = max(max_lcs, cur_lcs)
        return max_lcs
