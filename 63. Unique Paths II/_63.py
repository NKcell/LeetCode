class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        if not obstacleGrid[0]:
            return 0

        if obstacleGrid[0][0] == 1 or  obstacleGrid[-1][-1] == 1:
            return 0 

        for i in range(len(obstacleGrid)):
            if obstacleGrid[i][0] != 1:
                obstacleGrid[i][0] = 1
            else:
                for j in range(i, len(obstacleGrid)):
                    obstacleGrid[j][0] = 0
                break
        
        for i in range(1,len(obstacleGrid[0])):
            if obstacleGrid[0][i] != 1:
                obstacleGrid[0][i] = 1
            else:
                for j in range(i, len(obstacleGrid[0])):
                    obstacleGrid[0][j] = 0
                break

        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
        
        return obstacleGrid[-1][-1]

a = Solution()
print(a.uniquePathsWithObstacles([[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0],[0,1],[0,0],[0,0],[1,0],[0,0],[0,0],[0,1],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,1],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0]]))