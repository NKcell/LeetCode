class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        myLen = len(matrix)-1
        endLen = len(matrix)-1
        flag = len(matrix)
        start = 0
        while flag>1:
            for i in range(start, endLen):
                x = start
                y = i
                tmp = matrix[x][y]
                for _ in range(4):
                    now = matrix[y][myLen-x]
                    matrix[y][myLen-x] = tmp
                    tmp = now
                    x ,y = y, myLen-x
            start += 1
            flag -= 2
            endLen -= 1

    # 这个还是创造了新的空间 zip， 但用库的思想以及[::]的使用，要学习
    def rotate1(self, matrix):
        matrix[::] = zip(*matrix[::-1])

    def rotate2(self, A):
        A.reverse()
        for i in range(len(A)):
            for j in range(i):
                A[i][j], A[j][i] = A[j][i], A[i][j]