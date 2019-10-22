class Solution:
    def subsets(self, nums):
        nums.sort()
        myLen = len(nums)
        res = list()
        tmp = list()

        for i in nums:
            res.append([i])
            tmp.append([i])
        
        for _ in range(2, myLen+1):
            newtmp = list()
            for j in tmp:
                for x in range(nums.index(j[-1])+1, myLen):
                    res.append(j + [nums[x]])
                    newtmp.append(j + [nums[x]])
            tmp = newtmp
        
        res.append([])
        return res

    # DFS recursively 
    def subsets1(self, nums):
        res = []
        self.dfs(sorted(nums), 0, [], res)
        return res
        
    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i+1, path+[nums[i]], res)
            
    # Bit Manipulation    
    def subsets2(self, nums):
        res = []
        nums.sort()
        for i in range(1<<len(nums)):
            tmp = []
            for j in range(len(nums)):
                if i & 1 << j:  # if i >> j & 1:
                    tmp.append(nums[j])
            res.append(tmp)
        return res
        
    # Iteratively 这个方法好啊
    def subsets3(self, nums):
        res = [[]]
        for num in sorted(nums):
            res += [item+[num] for item in res]
        return res

    # def subsets4(self, nums):
    #     return reduce(lambda L, ele: L + [l + [ele] for l in L], nums, [[]])

    def subsets5(self, nums):
        import itertools
        return [[x for x in l if x is not None] for l in itertools.product(*zip(nums, [None] * len(nums)))]

    def subsets6(self, nums):
        import itertools
        return [l for n in range(len(nums) + 1) for l in itertools.combinations(nums, n)]

a = Solution()
print(a.subsets3([1,2,3]))
