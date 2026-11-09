class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        seen: set = set()
        for num in nums:
            seen.add(num)

        max_lcs: int = 0
        for num in nums:
            if num + 1 in seen:
                continue

            cur_lcs: int = 0
            cur_num: int = num
            while cur_num in seen:
                cur_lcs += 1
                cur_num -= 1
            max_lcs = max(max_lcs, cur_lcs)
        return max_lcs
