class Solution:
    def singleNumber(self, nums) -> int:
        myMap = {}
        for i in nums:
            v = myMap.get(i, 0)
            if v == 0:
                myMap[i] = 1
            else:
                myMap.pop(i)
        for i in myMap:
            return i

    # 异或这种方式很好
    def singleNumber2(self, nums):
        res = 0
        for num in nums:
            res ^= num
        return res