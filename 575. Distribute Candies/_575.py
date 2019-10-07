class Solution:
    def distributeCandies(self, candies) -> int:
        myDict = {}
        for i in candies:
            myDict[i] = 1

        return min(len(myDict), len(candies)//2)

    # 再次强调去重想set
    def distributeCandies1(self, candies):
        return min(len(candies)//2, len(set(candies)))