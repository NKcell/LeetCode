class Solution:
    def maxIncreaseKeepingSkyline(self, grid) -> int:
        l = list()
        for i in range(len(grid)):
            tmp = 0
            for j in range(len(grid[0])):
                tmp = max(tmp, grid[i][j])
            l.append(tmp)

        r = list()
        for i in range(len(grid[0])):
            tmp = 0
            for j in range(len(grid)):
                tmp = max(tmp, grid[j][i])
            r.append(tmp)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                count += min(l[i], r[j])-grid[i][j]

        return count

    def maxIncreaseKeepingSkyline1(self, grid):
        row, col = list(map(max, grid)), list(map(max, zip(*grid)))
        return sum(min(i, j) for i in row for j in col) - sum(map(sum, grid))