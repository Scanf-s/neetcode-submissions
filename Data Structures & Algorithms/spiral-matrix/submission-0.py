class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m: int = len(matrix)
        n: int = len(matrix[0])
        is_odd: bool = True if n % 2 != 0 else False
        ans: list[int] = []
        row_start: int = 0
        row_end: int = m - 1
        col_start: int = 0
        col_end: int = n - 1
        while row_start <= row_end and col_start <= col_end:
            
            for i in range(col_start, col_end + 1):
                ans.append(matrix[row_start][i])
                print(f"1: {matrix[row_start][i]}")
            
            for i in range(row_start + 1, row_end + 1):
                ans.append(matrix[i][col_end])
                print(f"2: {matrix[i][col_end]}")
            
            if row_end - row_start > 0:
                for i in range(col_end - 1, col_start - 1, -1):
                    ans.append(matrix[row_end][i])
                    print(f"3: {col_start} {col_end} {matrix[row_end][i]}")
            
            if col_end - col_start > 0:
                for i in range(row_end - 1, row_start, -1):
                    ans.append(matrix[i][col_start])
                    print(f"4: {matrix[i][col_start]}")
            
            print("########")
            row_start += 1
            row_end -= 1
            col_start += 1
            col_end -= 1

        return ans
            