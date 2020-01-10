class Solution:
    def letterCasePermutation(self, S: str):
        res = list()
        for i, v in enumerate(S):
            if not v.isdigit():
                res.append(i)
        
        ans = list()
        S = S.lower()
        for i in range(2**len(res)):
            tmp = bin(i)[2:]
            tmp = list(tmp)
            tmp.reverse()
            T = list(S)
            for index, v in enumerate(tmp):
                if v == '1':
                    T[res[index]] = T[res[index]].upper()
            ans.append(''.join(T))
        
        return ans

    def letterCasePermutation1(self, S):
        res = ['']
        for ch in S:
            if ch.isalpha():
                res = [i+j for i in res for j in [ch.upper(), ch.lower()]]
            else:
                res = [i+ch for i in res]
        return res

    def letterCasePermutation2(self, S):
        import itertools
        L = [[i.lower(), i.upper()] if i.isalpha() else i for i in S]
        return [''.join(i) for i in itertools.product(*L)]