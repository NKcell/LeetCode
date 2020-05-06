class Solution:
    def minCut(self, s: str) -> int:
        for i in range(0, len(s)):
            if self.xx(s, i):
                return i
        return 0

    def xx(self, s: str, i:int) -> bool:
        if i == 0:
            return self.ispar(s)

        for j in range(1, len(s)-i+1):
            if not self.ispar(s[:j]):
                continue
            if self.xx(s[j:], i-1):
                return True
        return False

    def ispar(self, s):
        l = 0
        r = len(s)-1
        while l<r:
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1
        return True

    def minCut1(self, s: str) -> int:
        res = [i for i in range(len(s))]

        for i in range(1, len(s)):
            if s[:i+1] == s[:i+1][::-1]:
                res[i] = 0
                continue
            res[i] = min([res[j-1]+1 for j in range(1,i+1) if s[j:i+1] == s[j:i+1][::-1]])

        return res[-1]

a = Solution()
print(a.minCut("fifgbeajcacehiicccfecbfhhgfiiecdcjjffbghdidbhbdbfbfjccgbbdcjheccfbhafehieabbdfeigbiaggchaeghaijfbjhi"))