class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        res = ['a']*len(S)
        pre = 0
        lst = len(S)-1
        while pre<=lst:
            flag = 0
            if not S[pre].isalpha():
                res[pre] = S[pre]
                pre+=1
                flag = 1
            if not S[lst].isalpha():
                res[lst] = S[lst]
                lst -= 1
                flag = 1
            
            if flag == 1:
                continue

            res[pre], res[lst] = S[lst], S[pre]
            pre += 1
            lst -= 1

        return ''.join(res)
    
    def reverseOnlyLetters1(self, S):
        S, i, j = list(S), 0, len(S) - 1
        while i < j:
            if not S[i].isalpha():
                i += 1
            elif not S[j].isalpha():
                j -= 1
            else:
                S[i], S[j] = S[j], S[i]
                i, j = i + 1, j - 1
        return "".join(S)

    def reverseOnlyLetters2(self, S):
        r = [s for s in S if s.isalpha()]
        return "".join(S[i] if not S[i].isalpha() else r.pop() for i in range(len(S)))

a = Solution()
print(a.reverseOnlyLetters("a-bC-dEf-ghIj"))