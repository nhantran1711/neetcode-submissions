class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        prefix = [0] * n
        prefix[0] = height[0]

        for i in range(1, n):
            prefix[i] = max(prefix[i - 1], height[i - 1])


        suffix = [0] * n
        suffix[-1] = height[-1]
        
        for i in range(n - 2, -1, -1):
            suffix[i] = max(suffix[i + 1], height[i + 1])

        water = [0] * n

        for i in range(n):
            water[i] = min(prefix[i], suffix[i]) - height[i]
        
        res = 0
        for i in range(n):
            if water[i] > 0:
                res += water[i]
        return res
