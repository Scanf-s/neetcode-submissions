class Solution:

    def recursion(self, nums: list[int], dup_check: set, cur: list[int], ans: list[list[int]]) -> None:
        sorted_cur: list[int] = sorted(cur)
        if tuple(sorted_cur) not in dup_check:
            ans.append(cur.copy())
            dup_check.add(tuple(sorted_cur))
        
        if not nums:
            return
        
        for idx in range(len(nums)):
            cur.append(nums[idx])
            self.recursion(nums[idx + 1:], dup_check, cur, ans)
            cur.pop()
    
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        ans: list[list[int]] = []
        dup_check: set = set()
        self.recursion(nums, dup_check, [], ans)
        return ans
