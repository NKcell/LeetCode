class Solution:
    def spiralOrder(self, matrix):
        res = list()
        while len(matrix) != 0 and len(matrix[0]) != 0:
            for i in matrix[0]:
                res.append(i)
            if len(matrix) == 0 or len(matrix[0]) == 0:
                break
            matrix = matrix[1:]

            for i in matrix:
                res.append(i[-1])
            if len(matrix) == 0 or len(matrix[0]) == 0:
                break
            matrix = [i[:-1] for i in matrix]

            for i in matrix[-1][::-1]:
                res.append(i)
            if len(matrix) == 0 or len(matrix[0]) == 0:
                break
            matrix = matrix[:-1]

            for i in matrix[::-1]:
                res.append(i[0])
            if len(matrix) == 0 or len(matrix[0]) == 0:
                break
            matrix = [i[1:] for i in matrix]
        return res

    # 这代码太神了，不太好懂，但思路很好
    def spiralOrder1(self, matrix):
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])

# Here's how the matrix changes by always extracting the first row and rotating the remaining matrix counter-clockwise:

#     |1 2 3|      |6 9|      |8 7|      |4|  =>  |5|  =>  ||
#     |4 5 6|  =>  |5 8|  =>  |5 4|  =>  |5|
#     |7 8 9|      |4 7|
# Now look at the first rows we extracted:

#     |1 2 3|      |6 9|      |8 7|      |4|      |5|
# Those concatenated are the desired result.

    def spiralOrder2(self, matrix):
        res = []
        if not matrix:
            return []
        i,j,di,dj = 0,0,0,1
        m, n = len(matrix),len(matrix[0])
        for _ in range(m * n):
            res.append(matrix[i][j])
            matrix[i][j] = ''
            if matrix[(i+di)%m][(j+dj)%n] == '':
                di, dj = dj, -di
            i += di
            j += dj
        return res

a = Solution()
print(a.spiralOrder([[1, 2, 3, 4],[5, 6, 7, 8],[9,10,11,12]]))