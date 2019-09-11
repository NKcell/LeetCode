class Solution:
    def maxProfit(self, prices) -> int:
        # if len(prices)<2:
        #     return 0
        # max = prices[1:]
        # max.sort()
        # max = max[-1]
        # maxmax = 0
        # for index,i in enumerate(prices):
        #     if i != max:
        #         if max-i>maxmax:
        #             maxmax = max-i
        #     else:
        #         if index<len(prices)-1:
        #             max = prices[index+1:]
        #             max.sort()
        #             max = max[-1]
        # return maxmax
        if len(prices) == 0:
            return 0
        min = prices[0]
        max = 0
        for i in prices:
            if min>=i:
                min = i
            else:
                if i-min>max:
                    max=i-min
        return max

a = Solution()
print(a.maxProfit([7,1,5,3,6,4]))