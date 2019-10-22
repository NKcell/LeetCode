class Solution:
    def repeatedNTimes(self, A) -> int:
        myDict = {}
        for i in A:
            v = myDict.get(i, 0)
            if v == 1:
                return i
            else:
                myDict[i] = 1

    # 这种随机的做法在数大的时候会很不错，而且空间消耗少
    def repeatedNTime1(self, A):
        import random
        while 1:
            s = random.sample(A, 2)
            if s[0] == s[1]:
                return s[0]

    # 时间复杂度来说感觉一般
    def repeatedNTimes2(self, A):
        return int((sum(A)-sum(set(A))) // (len(A)//2-1))