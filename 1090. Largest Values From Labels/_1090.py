class Solution:
    def largestValsFromLabels(self, values, labels, num_wanted, use_limit) -> int:
        valuedict = {}
        for i,v in enumerate(values):
            tmp = valuedict.get(v, 0)
            if tmp == 0:
                valuedict[v] = [i]
            else:
                valuedict[v] = (tmp+[i])
        labelsdict = {}
        for i,v in enumerate(labels):
            labelsdict[i] = v
        
        values = list(set(values))
        values.sort(reverse=True)
        resdict = {}
        count = 0
        res = 0

        for i in values:
            lable = valuedict[i]
            lablevalue = list()
            for k in lable:
                lablevalue.append(labelsdict[k])

            for j in lablevalue:
                tmp = resdict.get(j, 0)
                if tmp>=use_limit:
                    continue
                resdict[j] = tmp+1

                res += i
                count += 1
                
                if count >= num_wanted:
                    return res
        
        return res

        def largestValsFromLabels1(self, values, labels, num_wanted, use_limit):
            import collections
            counts = collections.defaultdict(int)
            vl = sorted(zip(values,labels))
            ans = 0
            while num_wanted and vl:
                val,lab = vl.pop()
                if counts[lab] < use_limit:
                    ans += val
                    counts[lab] += 1
                    num_wanted -= 1
            return ans

a = Solution()
print(a.largestValsFromLabels([0,6,7,5,7],[2,0,2,0,2],3,4))

