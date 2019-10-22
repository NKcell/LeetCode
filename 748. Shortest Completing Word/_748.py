class Solution:
    def shortestCompletingWord(self, licensePlate: str, words) -> str:
        licenseDict = {}
        for i in licensePlate:
            if 96<ord(i)<123:
                v = licenseDict.get(ord(i), 0)
                licenseDict[ord(i)] = v+1
            if 64<ord(i)<91:
                v = licenseDict.get(ord(i)+32, 0)
                licenseDict[ord(i)+32] = v+1

        res = list()
        for i in words:
            flag = 0
            for j in licenseDict:
                if licenseDict[j]>i.count(chr(j))+i.count(chr(j-32)):
                    flag = 1
                    break
            if flag == 0:
                res.append(i)
            
        res.sort(key = lambda i:len(i))
        return res[0]

    # 这代码真的是很Python
    # .lower()， .isalpha()来筛选元素
    # filter函数用的好
    # 下面一个列表生成式 里面的 & 用的很强啊 Counter特有啊， 学习了， 一直以为Counter和dict是一样的。。。
    # 然后min也用的很好，原来min也向sort一样可以加key函数
    def shortestCompletingWord1(self, licensePlate: str, words) -> str:
        from collections import Counter
        pc = Counter(filter(lambda x : x.isalpha(), licensePlate.lower()))
        return min([w for w in words if Counter(w) & pc == pc], key=len) 

    # 这个减法用的也是很有创意想法
    def shortestCompletingWord2(self, lp, words):
        import collections
        cnt = collections.Counter("".join(c for c in lp.lower() if c.isalpha()))
        return min([w for w in words if not cnt - collections.Counter(w)], key = len)

a = Solution()
print(a.shortestCompletingWord("1s3 456", ["looks", "pest", "stew", "show"]))