class Solution:
    def pancakeSort(self, A):
        res = list()
        count = len(A)
        self.getmin(A, res, count)
        return res

    def getmin(self, A, res,count):
        if count == 1:
            return
        index = A.index(count)
        if index != count-1:
            if index != 0:
                res.append(index+1)
                A = list(reversed(A[:index+1])) + A[index+1:]
            res.append(count)
            A = list(reversed(A[:count])) + A[count:]

        self.getmin(A, res, count-1)

    def pancakeSort1(self, A):
        res = []
        for x in range(len(A), 1, -1):
            i = A.index(x)
            res.extend([i + 1, x])
            A = A[:i:-1] + A[:i]
        return res