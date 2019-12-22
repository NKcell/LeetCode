class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        res = list()
        for i in s:
            res.append(''.join(list(i)[::-1]))
        return ' '.join(res)

    def reverseWords1(self, s):
        return ' '.join(s.split()[::-1])[::-1]

    def reverseWords2(self, s):
        return ' '.join(x[::-1] for x in s.split())