class Solution:
    def recursion(self, nums: list[int], cur: list[int], ans: list[list[int]]) -> None:
        if not nums:
            ans.append(cur.copy())
            return
        
        for idx in range(len(nums)):
            cur.append(nums[idx])
            self.recursion(nums[:idx] + nums[idx + 1:], cur, ans)
            cur.pop()

    def permute(self, nums: list[int]) -> list[list[int]]:
        ans: list[list[int]] = []
        self.recursion(nums, [], ans)
        return ans
