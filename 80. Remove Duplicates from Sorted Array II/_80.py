class Solution:
    def removeDuplicates(self, nums) -> int:
        if not nums:
            return 0
        
        pre = nums[0]
        fin = nums[-1]
        flag = 0
        i = 0
        while i<len(nums):
            if nums[i] == pre:
                flag += 1
            elif nums[i]<pre:
                return i
            else:
                flag = 1

            pre = nums[i]

            if flag < 3:
                i += 1
            else:
                if nums[i] == fin:
                    return i
                for j in range(i, len(nums)-1):
                    if nums[j]<=nums[j+1]:
                        nums[j], nums[j+1] = nums[j+1], nums[j]
                    else:
                        break
        return i

    # 看了别人的做法感觉自己是个zz
    # 题目没有要求说列表元素要保持一致，只能用换位去做题
    def removeDuplicates1(self, nums):
        i = 0
        for n in nums:
            if i < 2 or n > nums[i-2]:
                nums[i] = n
                i += 1
        return i

a = Solution()
nums =  [0,0,1,1,1,1,2,3,3]
print(nums[:a.removeDuplicates(nums)])