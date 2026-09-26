class Solution:
    def countBits(self, n: int) -> List[int]:
        
        res = [0] * (n + 1)
        for i in range(n + 1):
            res[i] = i.bit_count()
        return res