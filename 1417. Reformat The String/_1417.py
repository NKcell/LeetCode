class Solution:
    def reformat(self, s: str) -> str:
        letter = list()
        digit = list()

        for i in s:
            if '0'<=i<='9':
                digit.append(i)
            else:
                letter.append(i)

        if abs(len(letter)-len(digit)) > 1:
            return ""

        res = ""
        if len(letter)>len(digit):
            for i in digit:
                res += letter.pop()
                res += i
            res += letter.pop()
        elif len(letter)<len(digit):
            for i in letter:
                res += digit.pop()
                res += i
            res += digit.pop()
        else:
            for i in letter:
                res += digit.pop()
                res += i

        return res

a = Solution()
print(a.reformat("ab123"))