class Solution:
    def findShortestSubArray(self, nums) -> int:
        from collections import Counter
        nums_dict = Counter(nums)
        max_value = 0
        for key in nums_dict:
            if nums_dict[key]>max_value:
                max_value = nums_dict[key]
        
        re_value = len(nums)
        for key in nums_dict:
            if nums_dict[key] == max_value:
                tmp = self.getLength(nums, key)
                if tmp<re_value:
                    re_value = tmp
        return re_value

    def getLength(self, nums, max_value):
        pre = 0
        for index in range(len(nums)):
            if nums[index] == max_value:
                pre = index
                break
        for index in range(len(nums)-1,-1,-1):
            if nums[index] == max_value:
                return index-pre+1


    def findShortestSubArray1(self, nums):
        import collections
        first, last = {}, {}
        for i, v in enumerate(nums):
            first.setdefault(v, i)
            last[v] = i
        c = collections.Counter(nums)
        degree = max(c.values())
        return min(last[v] - first[v] + 1 for v in c if c[v] == degree)

    def findShortestSubArray2(self, nums):
        first, counter, res, degree = {}, {}, 0, 0
        for i, v in enumerate(nums):
            first.setdefault(v, i)
            counter[v] = counter.get(v, 0) + 1
            if counter[v] > degree:
                degree = counter[v]
                res = i - first[v] + 1
            elif counter[v] == degree:
                res = min(res, i - first[v] + 1)
        return res

a = Solution()
print(a.findShortestSubArray([1,2,2,1,2,1,1,1,1,2,2,2]))