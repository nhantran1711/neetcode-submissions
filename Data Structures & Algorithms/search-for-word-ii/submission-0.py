class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
    
    def add(self, word):
        cur = self
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.isEnd = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.add(w)
        
        m, n = len(board), len(board[0])
        res = set()
        visited = set()

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(i, j, node, word):
            if not (0 <= i < m) or not (0 <= j < n) or (i, j) in visited or board[i][j] not in node.children:
                return
            
            visited.add((i, j))
            node = node.children[board[i][j]]
            word += board[i][j]

            if node.isEnd:
                res.add(word)

            for dx, dy in directions:
                nx = dx + i
                ny = dy + j
                dfs(nx, ny, node, word)
            visited.remove((i, j))
            
        for i in range(m):
            for j in range(n):
                dfs(i, j, root, "")
        return list(res)