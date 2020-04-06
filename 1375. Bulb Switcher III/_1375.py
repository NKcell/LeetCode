class Solution:
    def numTimesAllBlue(self, light) -> int:
        maxNum = 1
        count = 0
        for i,v in enumerate(light):
            if v>maxNum:
                maxNum = v

            if i+1 >= maxNum:
                count += 1

        return count