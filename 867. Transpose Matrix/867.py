class Solution:
    def transpose(self, A):
        B = list()
        for i in range(len(A[0])):
            tmplist = list()
            for j in range(len(A)):
                tmplist.append(A[j][i])
            B.append(tmplist)

        return B
    
    def transpose1(self, A):
        return list(zip(*A))

a = Solution()
print(a.transpose1([[1,2,3],[4,5,6]]))

