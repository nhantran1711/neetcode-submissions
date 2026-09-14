class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        arr = []
        res = []

        def backtrack(openN, closeN):
            if openN == closeN == n:
                res.append(''.join(arr))
                return 
            
            if openN < n:
                arr.append("(")
                backtrack(openN + 1, closeN)
                arr.pop()
            
            if closeN < openN:
                arr.append(")")
                backtrack(openN, closeN + 1)
                arr.pop()

        backtrack(0, 0)
        return res