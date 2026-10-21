from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m: int = len(grid)
        n: int = len(grid[0])
        visited: list[list[bool]] = [[False for _ in range(n)] for _ in range(m)]
        ans: int = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    ans += 1
                    print(ans)
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
                                grid[nx][ny] == "1" and
                                not visited[nx][ny]
                            ):
                                visited[nx][ny] = True
                                q.append((nx, ny))
        return ans