class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        

        stack = []
        operators = '+-*/'

        for t in tokens:

            if t not in operators:
                stack.append(t)
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())

                if t == '+':
                    stack.append(str(num1 + num2))
                elif t == '-':
                    stack.append(str(num1 - num2))
                elif t == '*':
                    stack.append(str(num1 * num2))
                else:
                    stack.append(str(int(num1 / num2)))

        return int(stack[0])
                     