class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        a = abs(dividend)
        b = abs(divisor)

        res = 0
        while a>=b:
            a -= b
            res += 1

        if (dividend>=0 and divisor>0) or (dividend<=0 and divisor<0):
            return res
        else:
            return -res

    def divide1(self, A, B):
        if (A == -2147483648 and B == -1): return 2147483647
        a, b, res = abs(A), abs(B), 0
        for x in range(32)[::-1]:
            if (a >> x) - b >= 0:
                res += 1 << x
                a -= b << x
        return res if (A > 0) == (B > 0) else -res