class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        fin = 0
        tmp = 0
        for i in nums:
            if i == 1:
                tmp+=1
            else:
                if fin<tmp:
                    fin = tmp
                tmp = 0
        if tmp>fin:
            fin = tmp
        return fin

    def findMaxConsecutiveOnes1(self, nums):
        return len(max(''.join(map(str, nums)).split('0'), key=len))

a = Solution()
print(a.findMaxConsecutiveOnes([1,1,0,1,1,1]))