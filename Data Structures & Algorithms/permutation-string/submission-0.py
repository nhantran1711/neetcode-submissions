class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        counterS1 = collections.Counter(s1)
        counterS2 = {}

        win_size = len(s1)
        l = 0 

        for r in range(len(s2)):
            
            counterS2[s2[r]] = counterS2.get(s2[r], 0) + 1
            
            while (r - l + 1) > win_size:
                counterS2[s2[l]] -= 1
                
                if counterS2[s2[l]] == 0:
                    del counterS2[s2[l]]
                    
                l += 1

            
            if counterS1 == counterS2:
                return True
            
        return False
