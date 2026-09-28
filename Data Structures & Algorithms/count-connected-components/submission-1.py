class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        res = 0
        visited = [False] * n

        def dfs(node):
            for nei in adj_list[node]:
                if not visited[nei]:
                    visited[nei] = True
                    dfs(nei)
        
        for node in range(n):
            if not visited[node]:
                visited[node] = True
                dfs(node)
                res += 1
        return res
            