class Solution:

    def encode(self, strs: List[str]) -> str:
        length = []
        for s in strs:
            length.append(len(s))
        res = ''
        for i in range(len(length)):
            res += str(length[i])
            res += ','
        res += '#'
        for s in strs:
            res += s

        return res

    def decode(self, s: str) -> List[str]:
        # 5,5,#HelloWorld
        res = []

        length = []
        i = 0
        while s[i] != '#':
            j = i

            while s[j] != ',':
                j += 1
            l = int(''.join(s[i:j]))

            length.append(l)
            i = j + 1

        i += 1

        for j in length:
            word = ''.join(s[i:i + j])
            res.append(word)
            i = i + j
        return res
