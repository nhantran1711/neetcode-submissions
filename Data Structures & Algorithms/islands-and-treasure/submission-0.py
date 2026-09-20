class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        INF = 2147483647

        visited = set()

        def dfs(i, j):
            if not (0 <= i < m) or not (0 <= j < n) or grid[i][j] == -1 or (i, j) in visited:
                return INF
            
            if grid[i][j] == 0:
                return 0

            visited.add((i, j))
            cur = INF

            for dx, dy in directions:
                nx = dx + i
                ny = dy + j

                cur = min(cur, dfs(nx, ny) + 1)
            
            visited.remove((i, j))
            return cur
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == INF:
                    grid[i][j] = dfs(i, j)
            