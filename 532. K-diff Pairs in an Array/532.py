class Solution:
    def findPairs(self, nums, k: int):
        if k<0:
            return 0
        if k == 0:
            tmp = {}
            for i in nums:
                tmp[i] = tmp.get(i, 0)+1
            count = 0
            for value in tmp.values():
                if value>1:
                    count+=1
            return count
        nums = list(set(nums))
        tmp = []
        for i in nums:
            tmp.append(i+k)
        tmp = list(set(nums+tmp))
        return 2*len(nums)-len(tmp)

    # 上面都想到在k==0的时候用字典了，没有向下面方法一样巧妙啊
    def findPairs1(self, nums, k: int):
        import collections
        res = 0
        c = collections.Counter(nums)
        for i in c:
            if k > 0 and i + k in c or k == 0 and c[i] > 1:
                res += 1
        return res

    # c = collections.Counter(nums)
    # return  sum(k > 0 and i + k in c or k == 0 and c[i] > 1 for i in c)

    # 我方法的简洁版
    def findPairs2(self, nums, k):
        import collections
        if k>0:
            return len(set(nums)&set(n+k for n in nums))
        elif k==0:
            sum(v>1 for v in collections.Counter(nums).values())
        else:
            return 0

a = Solution()
print(a.findPairs([1, 3, 1, 5, 4],-1))