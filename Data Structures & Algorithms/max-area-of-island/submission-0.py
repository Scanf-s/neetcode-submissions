from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m: int = len(grid)
        n: int = len(grid[0])
        visited: list[list[bool]] = [[False for _ in range(n)] for _ in range(m)]
        max_area: int = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    cur_area: int = 1
                    q: deque = deque()
                    q.append((i, j))
                    visited[i][j] = True
                    while q:
                        cx, cy = q.popleft()
                        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                            nx, ny = cx + dx, cy + dy
                            if (
                                0 <= nx < m and
                                0 <= ny < n and
                                not visited[nx][ny] and
                                grid[nx][ny] == 1
                            ):
                                q.append((nx, ny))
                                visited[nx][ny] = True
                                cur_area += 1
                    max_area = max(max_area, cur_area)
        return max_area
