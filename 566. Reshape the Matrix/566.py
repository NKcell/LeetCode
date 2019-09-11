class Solution:
    def matrixReshape(self, nums, r: int, c: int) :
        import  copy
        if len(nums)*len(nums[0]) != r*c:
            return copy.deepcopy(nums)
        tmplist = []
        for i in nums:
            tmplist += i
        finlist = []
        for i in range(r):
            finlist.append(tmplist[c*i:c*(i+1)])
        return finlist

    # 这个方法真的是很好，很python，写法可读性虽然不好，但我喜欢
    def matrixReshape1(self, nums, r, c):
        return nums if len(sum(nums, [])) != r * c else map(list, zip(*([iter(sum(nums, []))]*c)))

    # 这个方法把列表表达式用到了极致吧...这个双循环列表表达式还是第一次见
    def matrixReshape2(self, nums, r, c):
        if r * c != len(nums) * len(nums[0]):
                return nums
        else:
            items = [y for x in nums for y in x]
            return [items[x*c : ((x+1)*c)] for x in range(r)]

a = Solution()
print(a.matrixReshape([[1,2],[3,4]],2,4))
