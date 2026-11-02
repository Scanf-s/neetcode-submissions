class Solution:
    def recursion(self, board: list[list[str]], visited: list[list[bool]], loc: tuple[int, int], idx: int, word: str) -> bool:
        if idx == len(word):
            return True

        cx, cy = loc
        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nx, ny = cx + dx, cy + dy
            if (
                0 <= nx < len(board) and
                0 <= ny < len(board[0]) and
                not visited[nx][ny] and
                board[nx][ny] == word[idx]
            ):
                visited[nx][ny] = True
                found: bool = self.recursion(board, visited, (nx, ny), idx + 1, word)
                visited[nx][ny] = False
                if found:
                    return True
    
        return False

    def exist(self, board: list[list[str]], word: str) -> bool:
        starting_points: list[tuple[int, int]] = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j]:
                    starting_points.append((i, j))
        
        for starting_point in starting_points:
            cur_word: str = word[0]
            visited: list[list[bool]] = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
            visited[starting_point[0]][starting_point[1]] = True
            if self.recursion(board, visited, starting_point, 1, word):
                return True

        return False