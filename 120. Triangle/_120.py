class Solution:
    def minimumTotal(self, triangle) -> int:
        for i,v in enumerate(triangle):
            if i == 0:
                continue

            for index,j in enumerate(v):
                if index==0:
                    v[0] = j+triangle[i-1][0]
                elif index == len(v)-1:
                    v[-1] = j+triangle[i-1][-1]
                else:
                    v[index] = j+min(triangle[i-1][index-1], triangle[i-1][index])

        return min(triangle[-1])

    def minimumTotal1(self, triangle):
        f = [0] * (len(triangle) + 1)
        for row in triangle[::-1]:
            for i in range(len(row)):
                f[i] = row[i] + min(f[i], f[i + 1])
        return f[0]