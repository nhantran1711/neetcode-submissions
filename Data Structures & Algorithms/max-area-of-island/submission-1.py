class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        res = 0
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()

        def dfs(i, j):
            if not (0 <= i < m) or not (0 <= j < n) or grid[i][j] == 0 or (i, j) in visited:
                return 0
            
            visited.add((i, j))
            cur = 1

            for dx, dy in directions:
                nx = dx + i
                ny = dy + j

                cur += dfs(nx, ny)
            
            return cur
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    res = max(res, dfs(i, j))
        return res

