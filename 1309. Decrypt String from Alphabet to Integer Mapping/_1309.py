class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = list()
        flag = 0
        for i in range(len(s)-1, -1, -1):
            if flag != 0:
                flag -= 1
                continue
            if s[i] == '#':
                res.append(chr(96+(int(s[i-1])+int(s[i-2])*10)))
                flag = 2
            else:
                res.append(chr(96+(int(s[i]))))

        res.reverse()
        return ''.join(res)

    def freqAlphabets1(self, s):
        import re
        return ''.join(chr(int(i[:2]) + 96) for i in re.findall(r'\d\d#|\d', s))


a = Solution()
print(a.freqAlphabets("25"))