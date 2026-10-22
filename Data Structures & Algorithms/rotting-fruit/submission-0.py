from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        num_fruits: int = 0
        minutes: int = 0
        m: int = len(grid)
        n: int = len(grid[0])
        q: deque = deque()
        visited: list[list[bool]] = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    num_fruits += 1
                if grid[i][j] == 2:
                    q.append((i, j, minutes))
                    visited[i][j] = True
        
        if num_fruits == 0:
            return minutes
        
        if not q:
            return -1
        
        while q:
            cx, cy, cur_minutes = q.popleft()
            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                nx, ny = cx + dx, cy + dy
                if (
                    0 <= nx < m and
                    0 <= ny < n and
                    not visited[nx][ny] and
                    grid[nx][ny] == 1
                ):
                    num_fruits -= 1
                    visited[nx][ny] = True
                    q.append((nx, ny, cur_minutes + 1))
                    if num_fruits == 0:
                        return cur_minutes + 1
        return -1
