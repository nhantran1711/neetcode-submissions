class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []

        def backtrack(start, path):
            if start == len(s):
                res.append(path.copy())
                return
            
            for end in range(start, len(s)):
                if self.check(s, start, end):
                    path.append(s[start:end + 1])
                    backtrack(end + 1, path)
                    path.pop()
            

        backtrack(0, [])
        return res


    
    def check(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True