class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        mymax = 0
        res = list()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and [i, j] not in res:
                    tmp = 1
                    res.append([i, j])
                    tmp = self.getArea(grid, i, j, tmp, res)
                    mymax = max(mymax, tmp)
        return mymax

    def getArea(self, grid, i, j, tmp, res) -> int:
        if i>0 and grid[i-1][j] == 1 and [i-1, j] not in res:
            res.append([i-1, j])
            tmp += 1
            tmp = self.getArea(grid, i-1, j, tmp, res)
        if i<len(grid)-1 and grid[i+1][j] == 1 and [i+1,j] not in res:
            res.append([i+1, j])
            tmp += 1
            tmp = self.getArea(grid, i+1, j, tmp, res)
        if j>0 and grid[i][j-1] == 1 and [i, j-1] not in res:
            res.append([i, j-1])
            tmp += 1
            tmp = self.getArea(grid, i, j-1, tmp, res)
        if j<len(grid[0])-1 and grid[i][j+1] == 1 and [i, j+1] not in res:
            res.append([i, j+1])
            tmp += 1
            tmp = self.getArea(grid, i, j+1, tmp, res)
        return tmp

    def maxAreaOfIsland1(self, grid):
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j]:
                grid[i][j] = 0
                return 1 + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i + 1, j) + dfs(i, j - 1)
            return 0

        areas = [dfs(i, j) for i in range(m) for j in range(n) if grid[i][j]]
        return max(areas) if areas else 0

a = Solution()
print(a.maxAreaOfIsland([[0,0,0,0,0,0,0,0]]))
