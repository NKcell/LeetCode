class Solution:
    def minSubsequence(self, nums):
        # mysum = sum(nums)
        # l = 0
        # r = 0
        # tmpSum = 0
        # mylen = 501
        # maxvalue = 0
        # index = list()


        # for i,v in enumerate(nums):
        #     r = i+1
        #     tmpSum += v
        #     if tmpSum > (mysum-tmpSum):
        #         while tmpSum-nums[l] > (mysum - tmpSum + nums[l]):
        #             tmpSum -= nums[l]
        #             l += 1

        #         if r-l < mylen:
        #             mylen = r-l
        #             index = [l, r]

        #         elif r-l == mylen:
        #             if tmpSum>maxvalue:
        #                 maxvalue = tmpSum
        #                 index = [l, r]

        #         tmpSum -= nums[l]
        #         l += 1

        # return sorted(nums[index[0]: index[1]], reverse=True)
        mySum = sum(nums)
        nums.sort()
        res = list()
        l = 0
        while l <= mySum:
            res.append(nums[-1])
            l += nums[-1]
            mySum -= nums.pop()
        return res


a = Solution()
print(a.minSubsequence([7,4,2,8,1,7,7,10]))
