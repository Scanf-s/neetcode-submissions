class Solution:

    def recursion(self, cur_subset: list[int], nums: list[int], results: list[list[int]]) -> None:
        if len(nums) == 0:
            results.append(cur_subset.copy())
            return
        
        results.append(cur_subset.copy())
        for idx in range(len(nums)):
            cur_subset.append(nums[idx])
            self.recursion(cur_subset, nums[idx + 1:], results)
            cur_subset.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        results: list[list[int]] = []
        self.recursion([], nums, results)
        return results
