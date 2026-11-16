class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water_area: int = 0
        start: int = 0
        end: int = len(heights) - 1
        while start < end:
            cur_area = (end - start) * min(heights[start], heights[end])
            max_water_area = max(max_water_area, cur_area)
            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1
        return max_water_area