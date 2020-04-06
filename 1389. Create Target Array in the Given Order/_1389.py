class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = list()

        for i,v in enumerate(index):
            res = res[0:v] + [nums[i]] + res[v:]

        return res
