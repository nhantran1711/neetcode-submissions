class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        res = []
        m, n = len(heights), len(heights[0])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def dfs(i, j, visited):
            if (i, j) in visited:
                return

            visited.add((i, j))
            for dx, dy in directions:
                nx = dx + i
                ny = dy + j
                if (0 <= nx < m) and (0 <= ny < n) and heights[nx][ny] >= heights[i][j]:
                    dfs(nx, ny, visited)
        
        pacVisited = set()
        atlVisited = set()


        for i in range(m):
            dfs(i, 0, pacVisited)
            dfs(i, n - 1, atlVisited)
        
        for j in range(n):
            dfs(0, j, pacVisited)
            dfs(m - 1, j, atlVisited)
        
        for i in range(m):
            for j in range(n):
                if (i, j) in pacVisited and (i, j) in atlVisited:
                    res.append([i, j])
        return res

        
