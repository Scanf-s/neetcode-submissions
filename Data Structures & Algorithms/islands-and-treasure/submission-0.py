from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        treasures: deque = deque()
        visited: list[list[bool]] = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    treasures.append((i, j, 0))
                    visited[i][j] = True

        while treasures:
            cx, cy, c_dist = treasures.popleft()
            for dx, dy in [(-1, 0), (0, 1), (0, -1), (1, 0)]:
                nx, ny = cx + dx, cy + dy
                if (
                    0 <= nx < len(grid) and
                    0 <= ny < len(grid[0]) and
                    not visited[nx][ny] and
                    grid[nx][ny] == 2 ** 31 - 1
                ):
                    grid[nx][ny] = c_dist + 1
                    treasures.append((nx, ny, c_dist + 1))

        return
        