class Solution:
    def shortestToChar(self, S, C):
        n, pos = len(S), -float('inf')
        res = [n] * n
        tmp = list()
        for i in range(n):
            tmp.append(i)
        tmp += tmp[::-1]
        for i in tmp:
            if S[i] == C:
                pos = i
            res[i] = min(res[i], abs(i - pos))
        return res

a = Solution()
print(a.shortestToChar(S = "loveleetcode", C = 'e'))