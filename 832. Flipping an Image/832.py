class Solution:
    def flipAndInvertImage(self, A):
        for index, value in enumerate(A):
            A[index] = value[::-1]
        for i in range(len(A)):
            for j in range(len(A[0])):
                A[i][j] = (A[i][j]+1)%2
        return A

    # 这个列表生成式和异或操作用的很6
    def flipAndInvertImage1(self, A):
        return [[1 ^ i for i in row[::-1]] for row in A]

a = Solution()
print(a.flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))