class Solution:
    def thirdMax(self, nums):
        tmp = set(nums)
        nums = list(tmp)
        nums.sort()
        if len(nums)<3:
            return nums[-1]
        else:
            return nums[-3]

################################################
    #相比上面的操作，set也是一个耗时的操作，加上sort，就不是一个O(N)了，而下面的操作只有一个for
    def thirdMax1(self, nums):
        m1 = m2 = m3 = -float("inf")
        for num in nums:
            if num > m1:
                m1, m2, m3 = num, m1, m2
            elif m2 < num < m1:
                m2, m3 = num, m2
            elif m3 < num < m2:
                m3 = num
        return m3 if m3 > -float("inf") else m1

a = Solution()
print(a.thirdMax([2, 1]))
        
