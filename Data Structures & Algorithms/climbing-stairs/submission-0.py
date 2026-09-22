class Solution:
    def climbStairs(self, n: int) -> int:
        
        ones, twos = 1, 2

        for i in range(3, n + 1):
            temp = ones + twos
            ones = twos
            twos = temp
        return twos