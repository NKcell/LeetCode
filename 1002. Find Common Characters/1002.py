class Solution:
    def commonChars(self, A):
        mydict = {}
        for i in A[0]:
            v = mydict.get(i, 0)
            mydict[i] = v+1

        for i in range(1, len(A)):
            tmpdict = {}
            for j in A[i]:
                v = tmpdict.get(j, 0)
                tmpdict[j] = v+1

            for k in mydict:
                mydict[k] = min(mydict[k], tmpdict.get(k, 0))

        a = ""
        for k in mydict:
            if mydict[k] != 0:
                a += mydict[k]*k

        return list(a)

    def commonChars2(self, A):
        d = {}
        for i in A:
            unique = list(set(i))
            for char in unique:
                if char in d.keys():
                    d[char] += [i.count(char)]
                else:
                    d[char] = [i.count(char)]
        ans = []
        for key in d.keys():
            if len(d[key]) == len(A):
                ans += [key]*min(d[key])
        return ans

a = Solution()
print(a.commonChars( ["cool","lock","cook"]))