class Solution:
    def hasGroupsSizeX(self, deck) -> bool:
        mymap = {}
        for i in deck:
            mymap[i] = mymap.get(i, 0)+1
        
        a = sorted(mymap,key=mymap.__getitem__)
        for i,v in enumerate(a):
            a[i] = mymap[v] 
            
        if a[0] == 1:
            return False
        gcdvalue = a[0]

        for i in a:
            gcdvalue = self.gcd(gcdvalue, i)
            if gcdvalue == 1:
                return False
        return True
    
    def gcd(self,a,b):
        while a!=0:
            a,b = b%a,a
        return b

    # 别人家的代码
    def hasGroupsSizeX1(self, deck):
        import collections
        from functools import reduce
        def gcd(a, b):
            while b: a, b = b, a % b
            return a
        count = collections.Counter(deck).values()
        return reduce(gcd, count) > 1
    
    # reduce函数和collections.Counter掌握用法啊！
    def hasGroupsSizeX2(self, deck):
        from math import gcd 
        from functools import reduce 
        import collections
        return reduce(gcd,collections.Counter(deck).values())>=2

a = Solution()
print(a.hasGroupsSizeX([1,1,1,1,2,2,2,2,2,2]))