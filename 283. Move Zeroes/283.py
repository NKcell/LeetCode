class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        # 用del 比 remove快很多
        count = []
        for i in range(len(nums)):
            if nums[i] == 0:
                count.append(i)
        flag = 0
        for i in count:
            del nums[i-flag]
            flag += 1
        nums += ([0]*len(count))
    
    def moveZeroes1(self, nums):
        # 第一次的方法，超时
        length = len(nums)
        count = 0
        for _ in range(length-1):    
            for i in range(length-1-count):
                if nums[i] == 0:
                    for i in range(i, length-1-count):
                        nums[i],nums[i+1] = nums[i+1],nums[i]
                    count += 1
                    break
    
    def moveZeroes2(self, nums):
        # 这个方法用remove，速度慢
        count = 0
        for i in nums:
            if i == 0:
                count += 1
        for _ in range(count):
            nums.remove(0)
        nums += ([0]*count)

    ###################################################################
    # 下面的方法很简洁很python，用自带的方法就很快，这个列表表达式用的很好，nums[:]保证了使用的是原地址
    def moveZeroes3(self, nums):
        count=nums.count(0)
        nums[:]=[i for i in nums if i != 0]
        nums+=[0]*count

    # 这个方法也是十分的好，前面我在想边找0边删除的时候发现会破坏循环很难操作，结果这里直接倒着进行找删操作就解决了看似很麻烦的问题
    def moveZeroes4(self, nums):
        for i in range(len(nums))[::-1]:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)

a = Solution()
b = [0,0,2,1,0,1,0,3,12,1,0]
a.moveZeroes(b)
print(b)
