class Solution:
    def minStartValue(self, nums) -> int:
        res = 0
        tmp = 0
        for i in nums:
            tmp += i
            if tmp<res:
                res = tmp

        return (res-1)*-1

a = Solution()
print(a.minStartValue([1,-2,-3]))