class Solution:
    def printVertically(self, s: str):
        sSplit = s.split(' ')
        maxLen = 0
        for i in sSplit:
            if len(i)>maxLen:
                maxLen = len(i)

        res = [""]*maxLen
        for i in range(maxLen):
            for value in sSplit:
                if len(value)>i:
                    res[i] += value[i]
                else:
                    res[i] += " "

        return [i.rstrip() for i in res]

    def printVertically1(self, s):
        import itertools
        return [''.join(a).rstrip() for a in itertools.zip_longest(*s.split(), fillvalue=' ')]
                    
a = Solution()
print(a.printVertically(s = "CONTEST IS COMING"))