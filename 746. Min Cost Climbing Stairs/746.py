class Solution:
    def minCostClimbingStairs(self, cost: list) -> int:
        for i in range(2, len(cost)):
            cost[i] = min(cost[i-1], cost[i-2]) + cost[i]
        return min(cost[-1],cost[-2])

    def func(self, cost):
        pre, cur = cost[0], cost[1]
        for i in range(2, len(cost)):
            pre, cur = cur, min(pre, cur) + cost[i]
        return min(pre,cur)

a = Solution()
print(a.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))