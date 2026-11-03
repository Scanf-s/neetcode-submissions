from itertools import permutations
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans: list[list[int]] = []
        for permutation in permutations(nums):
            ans.append(list(permutation))
        return ans