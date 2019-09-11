class Solution:
    def isToeplitzMatrix(self, matrix) -> bool:
        mydict = {}
        for index_row,row in enumerate(matrix):
            for index_col, value in enumerate(row):
                get_value = mydict.get((index_row-index_col), value)
                if value != get_value:
                    return False
                mydict[index_row-index_col] = get_value
        return True

    def isToeplitzMatrix1(self, m):
        for i in range(len(m) - 1):
            for j in range(len(m[0]) - 1):
                if m[i][j] != m[i + 1][j + 1]:
                    return False
        return True
    
    def isToeplitzMatrix2(self, m):
        return all(m[i][j] == m[i+1][j+1] for i in range(len(m)-1) for j in range(len(m[0])-1))
    
    def isToeplitzMatrix3(self, m):
        return all(r1[:-1] == r2[1:] for r1,r2 in zip(m, m[1:]))

a = Solution()
print(a.isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))

