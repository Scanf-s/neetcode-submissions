class Solution:

    def recursion(self, nums: list[int], start: int, cur: list[int], ans: list[list[int]]) -> None:
        ans.append(cur.copy())
        if start == len(nums):
            return
        
        for idx in range(start, len(nums)):
            if idx > start and nums[idx] == nums[idx - 1]:
                continue
            cur.append(nums[idx])
            self.recursion(nums, idx + 1, cur, ans)
            cur.pop()
    
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        ans: list[list[int]] = []
        self.recursion(sorted(nums), 0, [], ans)
        return ans
