class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        cols = set()
        pos = set()
        neg = set()

        res = []
        board = [["."] * n for _ in range(n)]
        
        def backtrack(r):
            if r == n:
                copy = [''.join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if (r + c) in pos or (r - c) in neg or c in cols:
                    continue

                pos.add((r + c))
                neg.add((r - c))
                cols.add(c)

                board[r][c] = 'Q'
                backtrack(r + 1)

                pos.remove((r + c))
                neg.remove((r - c))
                cols.remove(c)
                board[r][c] = '.'

        backtrack(0)
        return res


