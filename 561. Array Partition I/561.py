class Solution:
    def arrayPairSum(self, nums) -> int:
        nums.sort() 
        return sum([v for i,v in enumerate(nums) if i%2==0])
        # 这里写成sum[::2]更简洁
        # return sum([x for x in sorted(nums)[::2]])

a = Solution()
print(a.arrayPairSum([7,3,1,0,0,6]))