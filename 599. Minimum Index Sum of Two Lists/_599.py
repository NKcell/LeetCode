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

    # 这个用的是字典表达式？python确实灵活啊...
    def findRestaurant1(self, A, B):
        Aindex = {u: i for i, u in enumerate(A)}
        best, ans = 1e9, []

        for j, v in enumerate(B):
            i = Aindex.get(v, 1e9)
            if i + j < best:
                best = i + j
                ans = [v]
            elif i + j == best:
                ans.append(v)
        return ans

    # set取交集有意思
    def findRestaurant2(self, list1, list2):
        common  = list(set(list1).intersection(set(list2)))
        result = {word:list1.index(word) + list2.index(word) for word in common}
        if len(set(result.values())) == 1:
            return common
        return [(min(result,key=result.get))]

a = Solution()
print(a.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["KFC","Burger King","Tapioca Express","Shogun"]))