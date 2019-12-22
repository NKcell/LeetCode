class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum = 0
        pro = 1
        while n != 0:
            tmp = n%10
            sum += tmp
            pro *= tmp
            n = n//10
        return pro-sum

    def subtractProductAndSum1(self, n):
        from functools import reduce
        import operator
        A = list(map(int, str(n)))
        return reduce(operator.mul, A) - sum(A)