class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m: int = len(matrix)
        n: int = len(matrix[0])

        start: int = 0
        end: int = m * n - 1

        while start <= end:
            mid: int = (start + end) // 2

            row: int = mid // n
            col: int = mid % n

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                end = mid - 1
            else:
                start = mid + 1

        return False