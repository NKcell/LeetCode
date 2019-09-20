class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        nums.sort()
        numslen = len(nums)
        tmp = self.isanswer(nums, target, numslen)
        if tmp:
            return target
        closenum = 0
        while True:
            if closenum>=0:
                closenum = - (closenum+1)
            else:
                closenum = - (closenum-1)
            target = target+closenum
            #print(target)
            tmp = self.isanswer(nums, target, numslen)
            if tmp:
                return target
    def isanswer(self,nums,target,numslen):
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, numslen-1
            while l<r:
                v = nums[i] + nums[l] + nums[r]
                if v>target:
                    r-=1
                    while l<r and nums[r] == nums[r+1]:
                        r-=1
                elif v<target:
                    l+=1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
                else:
                    #print([nums[i], nums[l], nums[r]])
                    return [nums[i], nums[l], nums[r]]
        return []

a = Solution()
print(a.threeSumClosest([13,2,0,-14,-20,19,8,-5,-13,-3,20,15,20,5,13,14,-17,-7,12,-6,0,20,-19,-1,-15,-2,8,-2,-9,13,0,-3,-18,-9,-9,-19,17,-14,-19,-4,-16,2,0,9,5,-7,-4,20,18,9,0,12,-1,10,-17,-11,16,-13,-14,-3,0,2,-18,2,8,20,-15,3,-13,-12,-2,-19,11,11,-10,1,1,-10,-2,12,0,17,-19,-7,8,-19,-17,5,-5,-10,8,0,-12,4,19,2,0,12,14,-9,15,7,0,-16,-5,16,-12,0,2,-16,14,18,12,13,5,0,5,6],-59))