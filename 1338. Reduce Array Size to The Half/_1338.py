class Solution:
    def minSetSize(self, arr) -> int:
        myDict = dict()
        half = len(arr)/2

        for i in arr:
            tmp = myDict.get(i, 0)
            myDict[i] = tmp+1

        value = 0
        count = 0
        for k in sorted(myDict,key=myDict.__getitem__,reverse=True):
            value += myDict[k]
            count += 1
            if value>=half:
                return count