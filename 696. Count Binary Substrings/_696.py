class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        pre = 0
        res = list()
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                res.append(i-pre)
                pre = i
        res.append(len(s)-pre)
        fin = 0
        for i in range(1,len(res)):
            fin += min(res[i], res[i-1])
        return fin

    def countBinarySubstrings1(self, s):
        s = [len(i) for i in s.replace('01', '0 1').replace('10', '1 0').split()]
        return sum(min(a, b) for a, b in zip(s, s[1:]))

a = Solution()
print(a.countBinarySubstrings("10101"))