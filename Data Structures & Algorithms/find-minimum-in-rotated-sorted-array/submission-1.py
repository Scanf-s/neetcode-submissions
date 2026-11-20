class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        start: int = 0
        end: int = len(nums) - 1
        while start <= end:
            mid: int = (start + end) // 2
            if mid == 0 and nums[mid] > nums[end]:
                start = mid + 1
            else:
                if nums[mid] < nums[mid - 1]:
                    return nums[mid]
                else:
                    if nums[mid - 1] > nums[end]:
                        start = mid + 1
                    else:
                        end = mid - 1
        return -1
        