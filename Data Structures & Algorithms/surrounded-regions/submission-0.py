class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(i, j):
            if not (0 <= i < m) or not (0 <= j < n) or board[i][j] != 'O':
                return
            
            board[i][j] = 'T'
            for dx, dy in directions:
                nx = i + dx
                ny = j + dy
                dfs(nx, ny)
        
        for i in range(m):
            for j in range(n):
                if board[0][j] == 'O':
                    dfs(0, j)
                if board[m - 1][j] == 'O':
                    dfs(m - 1, j)
                if board[i][0] == 'O':
                    dfs(i, 0)
                if board[i][n - 1] == 'O':
                    dfs(i, n - 1)
                    
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'