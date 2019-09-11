class Solution:
    def prefixesDivBy5(self, A):
        tmp = 0
        relist = list()
        for i in A:
            tmp = (tmp<<1) + i
            if tmp%5 == 0:
                relist.append(True)
            else:
                relist.append(False)

        return relist

a = Solution()
print(a.prefixesDivBy5([0,1,1,1,1,1]))