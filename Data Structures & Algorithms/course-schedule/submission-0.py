class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        mp = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            mp[crs].append(pre)
        
        visiting = set()

        def dfs(course):
            if course in visiting:
                return False
            
            if mp[course] == []:
                return True
            
            visiting.add(course)
            for pre in mp[course]:
                if not dfs(pre):
                    return False

            visiting.remove(course)
            mp[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True