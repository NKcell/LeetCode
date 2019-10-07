class Solution:
    def islandPerimeter(self, grid) -> int:
        res = 0
        for col, v1 in enumerate(grid):
            for row, v in enumerate(v1):
                if v == 1:
                    if col == 0 or grid[col-1][row] == 0:
                        res+=1
                    if col == len(grid)-1 or grid[col+1][row] == 0:
                        res+=1
                    if row == 0 or grid[col][row-1] == 0:
                        res+=1
                    if row == len(grid[0])-1 or grid[col][row+1] == 0:
                        res+=1
        return res

    # 这里的zip解压用的有意思， 这相当与先算一遍行的边界（左右边界），再计算列的边界（上下边界）
    def islandPerimeter1(self, grid):
        grid_ext = ['0' + ''.join(str(x) for x in row) + '0' for row in grid]
        grid_trans = list(map(list, zip(*grid)))
        grid_ext += [ '0' + ''.join(str(x) for x in row) + '0' for row in grid_trans ]                
        return sum(row.count('01') + row.count('10') for row in grid_ext)