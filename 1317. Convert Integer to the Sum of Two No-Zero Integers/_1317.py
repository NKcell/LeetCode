class Solution:
    def getNoZeroIntegers(self, n: int):
        for i in range(1, 999):
            if '0' in str(i) or '0' in str(n-i):
                continue
            return [i, n-i]
    
    def getNoZeroIntegers1(self, n: int):
        if len(str(n)) == 1:
            return [1, n - 1]
        num = ""
        for i in str(n)[1:]:
            if i == "0":
                num += "1"
            elif i == "1":
                num += "2"
            elif i == "2":
                num += "3"
            else:
                num += "1"
        return [int(num), n - int(num)]
