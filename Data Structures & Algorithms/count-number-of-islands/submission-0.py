class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        res = 0
        visited = set()

        def dfs(i, j):
            if not (0 <= i < m) or not (0 <= j < n) or grid[i][j] == '0' or (i, j) in visited:
                return
            
            visited.add((i, j))
            
            for dx, dy in directions:
                nx = dx + i
                ny = dy + j

                dfs(nx, ny)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in visited:
                    dfs(i, j)
                    res += 1
        return res