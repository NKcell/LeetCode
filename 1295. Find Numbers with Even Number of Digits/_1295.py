class Solution:
    def findNumbers(self, nums) -> int:
        count = 0
        for i in nums:
            if len(str(i))%2 == 0:
                count += 1
        return count

    def findNumbers1(self, nums) -> int:
        return sum(len(str(n)) % 2 == 0 for n in nums) 