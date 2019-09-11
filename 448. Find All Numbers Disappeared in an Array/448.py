class Solution:
    def findDisappearedNumbers(self, nums):
        import collections
        mydic = collections.Counter(nums)
        renum = []
        for i in range(1,len(nums)+1):
            if mydic.get(i, -1) == -1:
                renum.append(i)
        return renum

    # 这个想法很好
    def findDisappearedNumbers1(self, nums):
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])
            
        return [i + 1 for i, num in enumerate(nums) if num > 0]

a = Solution()
print(a.findDisappearedNumbers1([4,3,2,7,8,2,3,1]))