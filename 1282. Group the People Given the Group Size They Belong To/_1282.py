class Solution:
    def groupThePeople(self, groupSizes):
        mydict = {}
        for i,v in enumerate(groupSizes):
            tmp = mydict.get(v, 0)
            if tmp:
                tmp.append(i)
                mydict[v] = tmp
            else:
                mydict[v] = [i]

        res = list()
        for i in mydict:
            start = 0
            while start<len(mydict[i]):
                if start+i<=len(mydict[i]):
                    res.append(mydict[i][start: start+i])
                else:
                    res.append(mydict[i][start: ])
                
                start += i
        
        return res

    def groupThePeople1(self, groupSizes):
        import collections
        count = collections.defaultdict(list)
        for i, size in enumerate(groupSizes):
            count[size].append(i)
        return [l[i:i + s]for s, l in count.items() for i in range(0, len(l), s)]

a = Solution()
print(a.groupThePeople(groupSizes = [2,1,3,3,3,2]))									