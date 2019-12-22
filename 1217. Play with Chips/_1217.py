class Solution:
    def minCostToMoveChips(self, chips) -> int:
        ans = [0,0]
        for i in chips:
            ans[i%2] += 1
        return min(ans)

    def minCostToMoveChips1(self, chips) -> int:
        odds = sum(x % 2 for x in chips)
        return min(odds, len(chips) - odds)