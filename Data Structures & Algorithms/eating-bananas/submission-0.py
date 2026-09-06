class Solution:
    def check(self, k, piles, h):
        
        total = 0
        for banana in piles:
            total += math.ceil(banana / k)
        return total <= h
        

    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        l, r = 1, max(piles)

        while l <= r:
            k = (l + r) // 2

            if self.check(k, piles, h):
                r = k - 1
            else:
                l = k + 1

        return l 



    
    