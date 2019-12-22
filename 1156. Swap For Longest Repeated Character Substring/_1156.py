class Solution:
    def maxRepOpt1(self, text: str) -> int:
        import collections
        mydict = collections.Counter(text)
        res = dict()

        start = 0
        for i in range(1, len(text)):
            if text[i] != text[i-1]:
                tmp = res.get(text[i-1], 0)
                if tmp == 0:
                    res[text[i-1]] = [start, i-1, min(i-start+1, mydict[text[i-1]])]
                else:
                    if start - tmp[1] == 2:
                        newlen = tmp[1]-tmp[0]+1+i-start+1
                        res[text[i-1]] = [start, i-1, max(tmp[2],min(newlen, mydict[text[i-1]]))]
                    else:
                        res[text[i-1]] = [start, i-1, max(tmp[2], min(i-start+1, mydict[text[i-1]]))]
                start = i

        tmp = res.get(text[start], 0)
        if tmp == 0:
            res[text[start]] = [start, len(text)-1, min(len(text)-start, mydict[text[start]])]
        else:
            if start - tmp[1] == 2:
                newlen = tmp[1]-tmp[0]+1+len(text)-start+1
                res[text[start]] = [start, len(text)-1, max(tmp[2], min(newlen, mydict[text[start]]))]
            else:
                res[text[start]] = [start, len(text)-1, max(tmp[2], min(len(text)-start, mydict[text[start]]))]

        maxv = 0
        for value in res.values():
            if value[2]>maxv:
                maxv = value[2]
        
        return maxv

    def maxRepOpt11(self, S):
        import itertools
        import collections
        # We get the group's key and length first, e.g. 'aaabaaa' -> [[a , 3], [b, 1], [a, 3]
        A = [[c, len(list(g))] for c, g in itertools.groupby(S)]
        # We also generate a count dict for easy look up e.g. 'aaabaaa' -> {a: 6, b: 1}
        count = collections.Counter(S)
        # only extend 1 more, use min here to avoid the case that there's no extra char to extend
        res = max(min(k + 1, count[c]) for c, k in A)
        # merge 2 groups together
        for i in range(1, len(A) - 1):
            # if both sides have the same char and are separated by only 1 char
            if A[i - 1][0] == A[i + 1][0] and A[i][1] == 1:
                # min here serves the same purpose
                res = max(res, min(A[i - 1][1] + A[i + 1][1] + 1, count[A[i + 1][0]]))
        return res

a = Solution()
print(a.maxRepOpt1(text = "abcdef"))