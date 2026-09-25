class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        INF = 2147483647

        def bfs(i, j):
            queue = collections.deque([(i, j)])
            visited = set()
            visited.add((i, j))

            cur = 0
            while queue:
                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    if grid[r][c] == 0:
                        return cur
                    
                    for dx, dy in directions:
                        nx = dx + r
                        ny = dy + c
                        if (0 <= nx < m) and  (0 <= ny < n) and (nx, ny) not in visited and grid[nx][ny] != -1:
                            visited.add((nx, ny))
                            queue.append([nx, ny])
                cur += 1
            return INF
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == INF:
                    grid[i][j] = bfs(i, j)