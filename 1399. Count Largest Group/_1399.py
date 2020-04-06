class Solution:
    def countLargestGroup(self, n: int) -> int:
        import collections
        myDict = collections.defaultdict(int)

        for i in range(1, n+1):
            tmp = 0
            while i != 0:
                tmp += (i%10)
                i = i//10

            myDict[tmp] += 1

        maxValue = max(myDict.values())

        res = 0
        for i in myDict:
            if myDict[i] == maxValue:
                res += 1

        return res