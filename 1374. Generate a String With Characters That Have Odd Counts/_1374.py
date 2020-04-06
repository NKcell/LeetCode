class Solution:
    def generateTheString(self, n: int) -> str:
        if n == 1:
            return "a"
        else:
            if n%2 == 0:
                return "a"*(n-1)+"b"
            else:
                return "a"+"b"+"c"*(n-2)

    def generateTheString1(self, n):
        return 'b' + 'ab'[n & 1] * (n - 1)