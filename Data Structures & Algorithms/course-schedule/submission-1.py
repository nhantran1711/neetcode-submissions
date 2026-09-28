class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preMap = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visited = set()
        visiting = set()

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

            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
