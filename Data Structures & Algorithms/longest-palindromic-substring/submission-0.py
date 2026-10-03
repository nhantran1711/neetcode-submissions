class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ''
        resLen = 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.check(''.join(s[i:j + 1])) and resLen < (j - i + 1):
                    resLen = j - i + 1
                    res = ''.join(s[i:j + 1])
        return res

    def check(self, word):
        l, r = 0, len(word) - 1
        while l < r:
            if word[l] != word[r]:
                return False
            l += 1
            r -= 1
        return True