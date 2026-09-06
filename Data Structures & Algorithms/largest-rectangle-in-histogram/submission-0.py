class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        n = len(heights)

        prefix = [-1] * n
        stack = []

        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            if stack:
                prefix[i] = stack[-1]

            stack.append(i)
        

        suffix = [n] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            if stack:
                suffix[i] = stack[-1]
            stack.append(i)

        res = 0

        for i in range(n):
            left = prefix[i] + 1
            right = suffix[i] - 1

            res = max(res, heights[i] * (right - left + 1))
        return res
