class Solution:
    def countNegatives(self, grid) -> int:
        myLen = len(grid[0])
        count = 0
        for i in grid:
            for index, value in enumerate(i):
                if value < 0:
                    count += myLen-index
                    break

        return count