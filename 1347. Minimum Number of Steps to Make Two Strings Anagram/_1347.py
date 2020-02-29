class Solution:
    def minSteps(self, s: str, t: str) -> int:
        a = [0]*26
        b = [0]*26
        for i in range(len(s)):
            a[ord(s[i])-97]+=1
            b[ord(t[i])-97]+=1

        res = 0
        for i in range(26):
            res += min(a[i], b[i])

        return len(s)-res

    def minSteps1(self, s: str, t: str) -> int:
        import collections
        import string
        res = 0
        s = collections.Counter(s)
        t = collections.Counter(t)
        for c in string.ascii_lowercase:
            res += s[c] - t[c] if s[c] > t[c] else 0
        return res

    def minSteps2(self, s: str, t: str) -> int:
        import collections
        s, t = map(collections.Counter, (s,t))
        diff = (s | t) - (s & t)
        return sum(diff.values())//2