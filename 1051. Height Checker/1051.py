class Solution:
    def heightChecker(self, heights) -> int:
        import copy
        heightsSort = copy.copy(heights)
        heightsSort.sort()
        count = 0
        for i in range(len(heights)):
            if heights[i] != heightsSort[i]:
                count += 1
        return count

a = Solution()
print(a.heightChecker([1,1,4,2,1,3]))