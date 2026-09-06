class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        cols = defaultdict(list)
        rows = defaultdict(list)
        sq = defaultdict(list)


        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                
                if (board[i][j] in rows[i]) or (board[i][j] in cols[j])  or (board[i][j] in sq[i // 3, j // 3]):
                    return False
                
                rows[i].append(board[i][j])
                cols[j].append(board[i][j])

                sq[i // 3, j // 3].append(board[i][j])
                print(sq)

        
        return True