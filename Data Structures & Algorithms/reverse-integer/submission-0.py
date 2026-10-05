class Solution:
    def reverse(self, x: int) -> int:
        
        res = list(str(x))
        l, r = 0, len(str(x)) - 1

        while l < r:
            res[l], res[r] = res[r], res[l]

            l += 1
            r -= 1
        
        res = int(''.join(res)) if res[-1] != '-' else -int(''.join(res[:len(res) - 1]))
        return res if -2**31 <= res <= 2**31 - 1 else 0
