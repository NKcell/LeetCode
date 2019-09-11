class Solution:
    def numMagicSquaresInside(self, grid) -> int:
        possible = list()
        count = 0
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                if grid[i+1][j+1] == 5:
                    possible.append((i+1,j+1))
        
        for i in possible:
            if  grid[i[0]][i[1]+1]+grid[i[0]][i[1]-1] == grid[i[0]-1][i[1]]+grid[i[0]+1][i[1]] == grid[i[0]+1][i[1]+1]+grid[i[0]-1][i[1]-1]:
                if sum(grid[i[0]-1][i[1]-1:i[1]+2]) == sum(grid[i[0]+1][i[1]-1:i[1]+2]) == (grid[i[0]-1][i[1]+1]+grid[i[0]][i[1]+1]+grid[i[0]+1][i[1]+1]):
                    if set((grid[i[0]+1][i[1]],grid[i[0]-1][i[1]],grid[i[0]+1][i[1]+1],grid[i[0]][i[1]+1],grid[i[0]-1][i[1]+1],grid[i[0]+1][i[1]-1],grid[i[0]][i[1]-1],grid[i[0]-1][i[1]-1],grid[i[0]][i[1]]))=={1,2,3,4,5,6,7,8,9}:
                        count+=1

        return count

    def numMagicSquaresInside1(self, g):
        def isMagic(i, j):
            s = "".join(str(g[i + x / 3][j + x % 3]) for x in [0, 1, 2, 5, 8, 7, 6, 3])
            return g[i][j] % 2 == 0 and (s in "43816729" * 2 or s in "43816729"[::-1] * 2)
        return sum(isMagic(i, j) for i in range(len(g) - 2) for j in range(len(g[0]) - 2) if g[i + 1][j + 1] == 5)


a = Solution()
print(a.numMagicSquaresInside([[1,8,6],[10,5,0],[4,2,9]]))