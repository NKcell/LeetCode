class Solution:
    def checkIfExist(self, arr) -> bool:
        myDict = dict()
        for i in arr:
            tmp = myDict.get(i, 0)
            if tmp:
                return True
            if i%2 == 0:
                myDict[i//2] = 1
            myDict[i*2] = 1
        
        return False

    def checkIfExist1(self, arr) -> bool:
        import collections
        s = collections.Counter(arr)
        #check if there are more than one zeros
        if(s[0]>1): 
            return True
        for num in arr:
            if s[2*num] and num!=0:
                return True
        return False