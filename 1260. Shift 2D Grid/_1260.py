class Solution:
    def shiftGrid(self, grid, k: int):
        res  = list()

        k = k%(len(grid)*len(grid[0]))

        for i in grid:
            for j in i:
                res.append(j)
        
        res = res[-k:] + res[:len(res)-k]

        s = list()
        for i in range(0, len(grid)):
            tmp = list()
            for j in range(0, len(grid[0])):
                tmp.append(res[i*len(grid[0])+j])
            s.append(tmp)

        return s

    def shiftGrid1(self, grid , k: int) :
        f1 = lambda col, nums: [nums[i:i+col] for i in range(0, len(nums), col)]
        f2 = lambda nums, k: nums[-k%len(nums):] + nums[:-k%len(nums)]
        return f1(len(grid[0]), f2(sum(grid, []), k))
