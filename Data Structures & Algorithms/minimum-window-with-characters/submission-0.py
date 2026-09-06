class Solution:
    def minWindow(self, s: str, t: str) -> str:



        if len(t) > len(s):
            return ''
        
        counterT = collections.Counter(t)
        counterS = {}

        have = 0
        need = len(counterT)

        res = ''
        resLen = float('inf')

        l = 0
        for r in range(len(s)):

            char = s[r]
            counterS[char] = counterS.get(char, 0) + 1

            if char in counterT and counterS[char] == counterT[char]:
                have += 1
            
            while have == need:

                if (r - l + 1) < resLen:
                    res = s[l: r + 1]
                    resLen = r - l + 1
                
                left_char = s[l]
                counterS[left_char] -= 1

                if counterT[left_char] and counterS[left_char] <  counterT[left_char]:
                    have -= 1
                
                l += 1
            
        return res






            
            
            


