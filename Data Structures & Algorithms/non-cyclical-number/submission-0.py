class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()
        cur = list(map(int, str(n).strip()))
        total = 0

        for num in cur:
            total += num ** 2
        seen.add(total)

        while total != 1:
            
            cur = list(map(int, str(total).strip()))
            total = 0
            
            for num in cur:
                total += num ** 2
            
            if total in seen:
                return False

            seen.add(total)

        return True
        
