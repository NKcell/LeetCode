class Solution:
    # 超时
    def threeSum(self, nums):
        myplus = {}
        mymins = {}
        for i in nums:
            if i>0:
                v = myplus.get(i, 0)
                myplus[i] = v+1
            else:
                v = mymins.get(i, 0)
                mymins[i] = v+1
        
        mylist = []
        for i in myplus:
            for j in mymins:
                value = j+i
                if value>=0:
                    v = mymins.get(-value, 0)
                    if v!=0:
                        if -value == j:
                            if v>1:
                                mylist.append([-value,-value,i])
                        else:
                            a =  [j,i,-value]
                            a.sort()
                            if a not in mylist:
                                mylist.append(a)
                if value < 0:
                    v = myplus.get(-value, 0)
                    if v!=0:
                        if -value == i:
                            if v>1:
                                mylist.append([-value,-value,j])
                        else:
                            a =  [j,i,-value]
                            a.sort()
                            if a not in mylist:
                                mylist.append(a)
            myplus[i] = 0

        if nums.count(0)>2:
            mylist.append([0,0,0])
        return mylist

    # 这个双层的思路是必须会的，记也要记住！
    def threeSum1(self, nums):
        nums.sort()
        numslen = len(nums)
        res = []
        for i in range(numslen - 2):
            if nums[i] > 0:
                break
            if i>0 and nums[i] == nums[i-1]:
                    continue
            l, r = i+1, numslen-1
            while r > l:  
                v = nums[i] + nums[r] + nums[l]
                if v > 0:
                    r -= 1
                    while r > l and nums[r] == nums[r+1]:
                        r -= 1
                elif v<0:
                    l += 1
                    while r > l and nums[l] == nums[l-1]:
                        l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while r > l and nums[l] == nums[l-1]:
                        l += 1
                    while r > l and nums[r] == nums[r+1]:
                        r -= 1
        return res

    # 这还是算用了两层循环，只不过第二层用了dict，类似two sum的做法
    def threeSum2(self, nums):
        numslen = len(nums)
        nums.sort()

        res = []

        for i in range(numslen-2):
            if nums[i]>0:
                break
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            mydict = {}
            j = i+1
            while j < numslen:
                v = mydict.get(0-nums[j]-nums[i], -1)
                if v == -1:
                    mydict[nums[j]] = j
                    j+=1
                else:
                    res.append([nums[i], nums[v] ,nums[j]])
                    j+=1
                    while j < numslen and nums[j] == nums[j-1]:
                        j+=1
        
        return res



a = Solution()
print(a.threeSum2([0,0,0]))

