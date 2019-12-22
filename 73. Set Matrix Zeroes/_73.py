class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = set()
        col = set()
        for colindex, v in enumerate(matrix):
            for rowindex, value in enumerate(v):
                if value == 0:
                    row.add(rowindex)
                    col.add(colindex)

        for i in row:
            for j in range(len(matrix)):
                matrix[j][i] = 0

        for i in col:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0


test = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
a = Solution()
a.setZeroes(test)
print(test)