class Solution:
    def diagonalSort(self, mat):
        for i in range(len(mat)):
            self.modifyMat(mat, i, 0)
        for i in range(len(mat[0])):
            self.modifyMat(mat, 0, i)
        return mat


    def modifyMat(self, mat, i, j):
        tmp = list()
        tmpi = i
        tmpj = j
        while i<len(mat) and j<len(mat[0]):
            tmp.append(mat[i][j])
            i+=1
            j+=1
        tmp.sort()
        count = 0
        while tmpi<len(mat) and tmpj<len(mat[0]):
            mat[tmpi][tmpj] = tmp[count]
            count+=1
            tmpi+=1
            tmpj+=1


    def diagonalSort1(self, A):
        import collections
        n, m = len(A), len(A[0])
        d = collections.defaultdict(list)
        for i in range(n):
            for j in range(m):
                d[i - j].append(A[i][j])
        for k in d:
            d[k].sort(reverse=1)
        for i in range(n):
            for j in range(m):
                A[i][j] = d[i - j].pop()
        return A

    def diagonalSort2(self, A):
        m, n = len(A), len(A[0])
        def sort(i, j):
            vals = []
            while i < m and j < n:
                vals.append(A[i][j])
                i += 1
                j += 1
            vals.sort()
            while i and j:
                j -= 1
                i -= 1
                A[i][j] = vals.pop()
        for i in range(m): sort(i, 0)
        for j in range(n): sort(0, j)
        return A

a = Solution()
print(a.diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]]))