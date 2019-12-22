class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        res1 = list()
        res2 = list()
        self.getSub(res1, str1)
        self.getSub(res2, str2)
        res1 = set(res1)
        res2 = set(res2)
        res = list((res1&res2))
        if res:
            res.sort()
            return res[-1]
        return ""

    def getSub(self, res, mystr):
        mylen = len(mystr)
        for i in range(mylen):
            if mylen%(i+1) == 0 and mystr[0:i+1]*(mylen//(i+1)) == mystr:
                res.append(mystr[0:i+1])

    # 两种思路啊，一个就GCD，一个暴力破解，上面我的做法类似暴力破解，但写的思路不是很明确啊
    # 下面就是GCD的思路
    def gcdOfStrings1(self, str1: str, str2: str) -> str:
        if len(str1) == len(str2):
            return str1 if str1==str2 else ''
        else:
            if len(str1) < len(str2):
                str1,str2 = str2,str1
            if str1[:len(str2)] == str2:
                return self.gcdOfStrings(str1[len(str2):],str2)
            else:
                return ''

a = Solution()
print(a.gcdOfStrings(str1 = "LEET", str2 = "CODE"))