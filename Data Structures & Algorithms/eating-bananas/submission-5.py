import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start: int = 1
        end: int = max(piles)
        result: int = 10 ** 9 + 1

        while start <= end:
            k: int = (start + end) // 2
            cur_h: int = 0
            for pile in piles:
                if k > pile:
                    cur_h += 1
                else:
                    cur_h += math.ceil(pile / k)

            if cur_h <= h:
                result = min(k, result)
                end = k - 1
            else:
                start = k + 1

        return result
