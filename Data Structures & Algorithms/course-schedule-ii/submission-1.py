class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visited = set()
        visiting = set()
        res = []

        def dfs(course):
            if course in visiting:
                return False
            
            if course in visited:
                return True
            

            visiting.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            
            visiting.remove(course)
            visited.add(course)
            res.append(course)
            
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return res