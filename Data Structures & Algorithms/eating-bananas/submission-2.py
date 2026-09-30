class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def check(hour):
            res = 0
            for p in piles:
                res += math.ceil(p / hour)
            return res
        
        l, r = 1, max(piles)

        while l <= r:
            m = (l + r) // 2
            if check(m) <= h:
                r = m - 1
            else:
                l = m + 1
        return l