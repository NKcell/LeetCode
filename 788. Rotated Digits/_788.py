class Solution:
    def rotatedDigits(self, N: int) -> int:
        count = 0
        for i in range(N+1):
            i = str(i)
            flag = 0
            for j in ["3","4","7"]:
                if j in i:
                    flag = 1
                    break
            if flag == 1:
                continue

            for k in i:
                if k in ["2","5","6","9"]:
                    count+=1
                    break
        return count

    def rotatedDigits1(self, N):
        s1 = set([1, 8, 0])
        s2 = set([1, 8, 0, 6, 9, 2, 5])
        def isGood(x):    
            s = set([int(i) for i in str(x)])
            return s.issubset(s2) and not s.issubset(s1)
        return sum(isGood(i) for i in range(N + 1))