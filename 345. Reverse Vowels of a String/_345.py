class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        myvowels = list()
        for i in s:
            if i in vowels:
                myvowels.append(i)
        
        myvowels.reverse()
        flag = 0
        s = list(s)
        for i,v in enumerate(s):
            if v in vowels:
                s[i] = myvowels[flag]
                flag += 1
        
        return ''.join(s)

    def reverseVowels1(self, s: str) -> str:
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        res = list(s)
        i1 = 0
        i2 = len(res)-1
        while i1<i2:
            if (res[i1] in vowels) and (res[i2] in vowels):
                res[i1], res[i2] = res[i2], res[i1]
                i1+=1
                i2-=1
                continue
            if not (res[i1] in vowels):
                i1+=1
            if not (res[i2] in vowels):
                i2-=1
        return ''.join(res)

    def reverseVowels2(self, s):
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        L = list(s)
        i = 0
        j = len(L) - 1
        while i < j:
            while i < j and L[i] not in vowels:
                i += 1
            while j > i and L[j] not in vowels:
                j -= 1
            L[i], L[j] = L[j], L[i] 
            i += 1
            j -= 1
        return ''.join(L)

a = Solution()
print(a.reverseVowels1('hello'))