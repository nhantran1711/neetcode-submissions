class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m = len(board)
        n = len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        visited = set()

        def backtrack(i, j, index):
            if index == len(word):
                return True

            if not (0 <= i < m) or not (0 <= j < n) or (board[i][j] != word[index]) or ((i, j) in visited):
                return False

            visited.add((i, j))
            res = False
            for dx, dy in directions:
                nx = i + dx
                ny = j + dy

                if backtrack(nx, ny, index + 1):
                    res = True
            
            visited.remove((i, j))
            return res
        
        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True
        return False

