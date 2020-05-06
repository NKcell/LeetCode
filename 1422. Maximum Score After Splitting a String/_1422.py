class Solution:
    def maxScore(self, s: str) -> int:
        res = [0]*(len(s)+1)
        res[0] = s.count('1')
        for i,v in enumerate(s):
            if v == '0':
                res[i+1] = res[i]+1
            else:
                res[i+1] = res[i]-1

        return max(res[1:-1])

a = Solution()
print(a.maxScore("1111"))