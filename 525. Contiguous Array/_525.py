class Solution:
    def findMaxLength(self, nums) -> int:
        maxLength = 0
        myDict = dict()
        count = 0
        myDict[0] = 0

        for i,v in enumerate(nums, 1):
            if v == 0:
                count -= 1
            else:
                count += 1

            tmp = myDict.get(count, -1)
            if tmp == -1:
                myDict[count] = i
            else:
                maxLength = max(maxLength, i-tmp)

        return maxLength