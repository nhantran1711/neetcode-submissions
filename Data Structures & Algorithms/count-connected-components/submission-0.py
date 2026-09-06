class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.count = n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        nodeA, nodeB = self.find(x), self.find(y)

        if nodeA == nodeB:
            return
        
        self.parent[nodeA] = nodeB
        self.count -= 1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        uf = UnionFind(n)

        for u, v in edges:
            uf.union(u, v)
        
        return uf.count