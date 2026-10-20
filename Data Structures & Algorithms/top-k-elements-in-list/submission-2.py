from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency: dict = Counter(nums)
        minheap: list[int] = []
        for num, freq in frequency.items():
            heapq.heappush(minheap, (freq, num))
            if len(minheap) > k:
                heapq.heappop(minheap)
        return [num for _, num in minheap]
