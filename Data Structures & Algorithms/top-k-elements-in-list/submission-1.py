import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq: dict = Counter(nums)
        sorted_freq = dict(sorted(freq.items(), key=lambda x: -x[1]))
        ans: list[int] = []
        for num in sorted_freq.keys():
            if len(ans) == k:
                break
            ans.append(num)
        return ans