class Solution:
    def countServers(self, grid) -> int:
        m = list()
        n = list()

        for i in range(len(grid)):
            count = 0
            for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        count+=1
            if count>1:
                m.append(i)

        for i in range(len(grid[0])):
            count = 0
            for j in range(len(grid)):
                    if grid[j][i] == 1:
                        count+=1
            if count>1:
                n.append(i)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if i in m:
                        count+=1
                    elif j in n:
                        count+=1
        return count

    def countServers1(self, A):
        X, Y = list(map(sum, A)), list(map(sum, zip(*A)))
        return sum(X[i] + Y[j] > 2 for i in range(len(A)) for j in range(len(A[0])) if A[i][j])

    def countServers2(self, grid) -> int:
        R, C, res = len(grid), len(grid[0]), 0
        for r in range(R):
            for c in range(C):
                if grid[r][c]:
                    res += any(grid[i][c] for i in range(R) if i != r) or any(grid[r][j] for j in range(C) if j != c)
        return res

a = Solution()
print(a.countServers([[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]))