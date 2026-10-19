class Solution:
    def recursion(self, cur_selected: list[int], nums: list[int], start: int, remaining: int, results: list[list[int]]) -> None:
        if remaining == 0:
            results.append(cur_selected.copy())
            return
        
        if remaining < 0:
            return

        for idx in range(start, len(nums)):
            cur_selected.append(nums[idx])
            self.recursion(cur_selected, nums, idx, remaining - nums[idx], results)
            cur_selected.pop()

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results: list[list[int]] = []
        self.recursion([], nums, 0, target, results)
        return results
