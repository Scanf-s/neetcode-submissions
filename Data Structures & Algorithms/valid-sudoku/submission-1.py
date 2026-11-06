class Solution:
    def check(self, candidate: list[str]) -> bool:
        seen: set = set()
        for el in candidate:
            if el == '.':
                continue
            if el in seen:
                return False
            seen.add(el)
        return True

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # check row
        for i in range(len(board)):
            if not self.check(board[i]):
                return False
        
        # check col
        for i in range(len(board[0])):
            candidate: list[str] = []
            for j in range(len(board)):
                candidate.append(board[j][i])
            if not self.check(candidate):
                return False

        # check grid
        for i in range(0, len(board), 3):
            for j in range(0, len(board[0]), 3):
                
                candidate: list[str] = []
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        candidate.append(board[r][c])
                
                if not self.check(candidate):
                    return False
                
        return True
