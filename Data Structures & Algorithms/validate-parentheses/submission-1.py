class Solution:
    def isValid(self, s: str) -> bool:
        
        bracket = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        stack = []


        for char in s:
            if stack and char in bracket and bracket[char] == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
        
        return len(stack) == 0