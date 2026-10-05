class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        

        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        print(adj_list)

        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node)
            for nei in adj_list[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        
        return dfs(0, -1)