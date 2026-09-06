class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ''
        for char in s:
            if char.isalpha():
                temp += char.lower()
            elif char.isnumeric():
                temp += str(char)
        return temp == temp[::-1]