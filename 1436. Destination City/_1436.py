class Solution:
    def destCity(self, paths) -> str:
        myDict = dict()
        for i in paths:
            tmp = myDict.get(i[0], None)
            if tmp:
                del myDict[i[0]]
            else:
                myDict[i[0]] = 1

            tmp = myDict.get(i[1], None)
            if tmp:
                del myDict[i[1]]
            else:
                myDict[i[1]] = 2


        for i in myDict:
            if myDict[i] == 2:
                return i

    def destCity1(self, paths) -> str:
        A, B = map(set, zip(*paths))
        return (B - A).pop()

a = Solution()
print(a.destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))
