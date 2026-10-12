class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        if "0" == num1[0] or "0" == num2[0]:
            return "0"

        m, n = len(num1), len(num2)

        res = [0] * (m + n)

        num1, num2 = num1[::-1], num2[::-1]

        for i in range(m):
            for j in range(n):
                res[i + j] += int(num1[i]) * int(num2[j])
                carry = res[i + j] // 10
                res[i + j + 1] += carry
                res[i + j] = res[i + j] % 10


        res = res[::-1]
        i = 0
        while i < len(res) and res[i] == 0:
            i += 1
        
        res = list(map(str, res[i:]))
        return ''.join(res)
