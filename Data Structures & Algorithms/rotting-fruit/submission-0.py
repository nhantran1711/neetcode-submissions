class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        fresh = 0

        queue = collections.deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1
        
        t = 0
        while fresh and queue:
            level = len(queue)

            for _ in range(level):
                i, j = queue.popleft()

                for dx, dy in directions:
                    nx = i + dx
                    ny = j + dy
                    if (0 <= nx < m) and (0 <= ny < n) and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        queue.append((nx, ny))
                        fresh -= 1
                    
            t += 1
        
        return t if fresh == 0 else -1