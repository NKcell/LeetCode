class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) == 0:
            return 0
        profit = 0
        start = prices[0]
        for i in prices:
            if i>start:
                profit += i-start
            start = i

        return profit

a = Solution()
print(a.maxProfit([7,6,4,3,1]))

############################################
# return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))
# return sum([b-a for a,b in zip(prices,prices[1:]) if b-a > 0])

# 这两个一行的语句都很pythonic