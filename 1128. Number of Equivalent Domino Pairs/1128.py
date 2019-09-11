class Solution:
    def numEquivDominoPairs(self, dominoes) -> int:
        mydict = {}
        for i in dominoes:
            tmp1 = i[0]*10+i[1]
            tmp2 = i[1]*10+i[0]
            v1 = mydict.get(tmp1, 0)
            v2 = mydict.get(tmp2, 0)
            if v1==0 and v2==0:
                mydict[tmp1] = 1
            elif v1 != 0:
                mydict[tmp1] = v1+1
            else:
                mydict[tmp2] = v2+1

        count = 0
        for i in mydict:
            count += mydict[i]*(mydict[i]-1)//2
        return count

    # 这个用到来不可变集合frozenset，利用来它可以作为字典key的特性，第一次见到吧
    # 同时利用来集合的无序性，所以整体代码肯定比我上面的要好
    # 一个对象能不能作为字典的key，就取决于其有没有__hash__方法。
    # 所以所有python自带类型中，除了list、dict、set和内部至少带有上述三种类型之一的tuple之外，其余的对象都能当key。
    # 所以还可以用tuple
    def numEquivDominoPairs1(self, dominoes) -> int:
        dominoes_count = 0
        sets = {}
        for pair in dominoes:
            this_set = frozenset(pair)
            if this_set in sets:
                dominoes_count += sets[this_set]
                sets[this_set] += 1
            else:
                sets[this_set] = 1
        return dominoes_count

a = Solution()
print(a.numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6]]))