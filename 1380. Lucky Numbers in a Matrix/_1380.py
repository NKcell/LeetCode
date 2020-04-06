class Solution:
    def luckyNumbers (self, matrix) :
        res = list()
        for i in range(len(matrix) ):
            tmp = min(matrix[i])
            index = matrix[i].index(tmp)
            if index>len(matrix[0]):
                continue
            if tmp == max([j[index] for j in matrix]):
                res.append(tmp)

        return res

    def luckyNumbers1(self, matrix):
        return list({min(row) for row in matrix} & {max(col) for col in zip(*matrix)})

    def luckyNumbers2(self, matrix):
        mi = [min(row) for row in matrix]
        mx = [max(col) for col in zip(*matrix)]
        return [cell for i, row in enumerate(matrix) for j, cell in enumerate(row) if mi[i] == mx[j]]

a = Solution()
print(a.luckyNumbers([[7,8],[1,2]]))