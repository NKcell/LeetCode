class Solution:
    def canJump(self, nums) -> bool:
        lenNums = len(nums)-1
        stratindex = 0
        endindex = nums[0]
        while True:
            if endindex >= lenNums:
                return True
            bigvalue = -1
            for i in range(stratindex, endindex+1):
                tmp = nums[i]+i
                if tmp >= lenNums:
                    return True
                if tmp > bigvalue:
                    bigvalue = tmp
            stratindex = endindex
            endindex = bigvalue
            if stratindex>=bigvalue:
                return False

    # 贪婪算法
    def canJump1(self, nums) -> bool:
        lenNums = len(nums)-1
        for i in range(lenNums, -1, -1):
            if nums[i]+i >= lenNums:
                lenNums = i
        return lenNums == 0