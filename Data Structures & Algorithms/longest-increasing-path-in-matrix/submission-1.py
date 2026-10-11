class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        m, n = len(matrix), len(matrix[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


        dp = {}

        def dfs(i, j, prev):
            if not (0 <= i < m) or not (0 <= j < n) or (matrix[i][j] <= prev):
                return 0
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            res = 1

            for dx, dy in directions:
                nx = dx + i
                ny = dy + j

                res = max(res, dfs(nx, ny, matrix[i][j]) + 1)
            dp[(i, j)] = res
            return res
        
        for i in range(m):
            for j in range(n):
                dfs(i, j, -1)

        return max(dp.values())