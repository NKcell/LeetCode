class Solution:
    def findRestaurant(self, list1, list2):
        myDict = {}
        myDict1 = {}
        for i, v in enumerate(list1):
            myDict[v] = i
        for i, v in enumerate(list2):
            dictv = myDict.get(v, -1)
            if dictv != -1:
                myDict1[v] = dictv+i
        minvalue = 2000
        res = list
        for i in myDict1:
            if myDict1[i]<minvalue:
                minvalue = myDict1[i]
                res = [i]
            elif myDict1[i] == minvalue:
                res.append(i)
        return res

a = Solution()
print(a.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["KFC","Burger King","Tapioca Express","Shogun"]))