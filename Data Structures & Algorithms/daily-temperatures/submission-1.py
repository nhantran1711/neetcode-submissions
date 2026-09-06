class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        res = [0] * n

        stack = []

        for i in range(len(temperatures)):

            while stack and temperatures[stack[-1]] < temperatures[i]:
                temp = stack.pop()
                res[temp] = i - temp
            
            stack.append(i)
        return res
