class Solution:
    def findDuplicate(self, nums) -> int:
        res = dict()
        for i in nums:
            tmp = res.get(i, 0)
            if tmp == 0:
                res[i] = 1
            else:
                return i

    def findDuplicate1(self, nums):
        low = 0
        high = len(nums) - 1
        mid = (high + low) / 2
        while high - low > 1:
            count = 0
            for k in nums:
                if mid < k <= high:
                    count += 1
            if count > high - mid:
                low = mid
            else:
                high = mid
            mid = (high + low) / 2
        return high