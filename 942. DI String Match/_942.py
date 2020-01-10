class Solution:
    def diStringMatch(self, S: str):
        res = [0]*(len(S)+1)
        mymax = 0
        mymin = 0
        for i,v in enumerate(S):
            if v == 'I':
                mymax += 1
                res[i+1] = mymax
            else:
                mymin -= 1
                res[i+1] = mymin

        for i,v in enumerate(res):
            res[i] = v-mymin

        return res

    def diStringMatch1(self, S):
        left = right = 0
        res = [0]
        for i in S:
            if i == "I":
                right += 1
                res.append(right)
            else:
                left -= 1
                res.append(left)
        return [i - left for i in res]

    def diStringMatch2(self, S):
        l, r, arr = 0, len(S), []
        for s in S:
            arr.append(l if s == "I" else r)
            l, r = l + (s == "I"), r - (s == "D")
        return arr + [l]