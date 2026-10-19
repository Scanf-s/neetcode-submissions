class Solution:
    def recursion(self, cur_nums: list[int], nums: list[int], start_idx: int, remaining: int, results: list[list[int]]) -> None:
        if remaining == 0:
            results.append(cur_nums)
            return
        
        if remaining < 0:
            return

        for idx in range(start_idx, len(nums)):
            if idx > start_idx and nums[idx] == nums[idx - 1]:
                continue
            self.recursion(cur_nums + [nums[idx]], nums, idx + 1, remaining - nums[idx], results)
        
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sorted_candidates = sorted(candidates)
        results: list[list[int]] = []
        self.recursion([], sorted_candidates, 0, target, results)
        return results
