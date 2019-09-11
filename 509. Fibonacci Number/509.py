class Solution:
    def fib(self, N: int) -> int:
        a = 0
        b = 1
        if N == 0:
            return a
        if N == 1:
            return b
        for _ in range(N-1):
            a, b = b, a+b
        return b
    
    ################################
    def fib1(self, N):
        a,b = 0,1
        for _ in range(N):
            a, b = b, a+b
        return a 
    
    # 递归
    def fib2(self, N):
        if N == 0: return 0
        if N == 1: return 1
        return self.fib2(N-1) + self.fib2(N-2)

a = Solution()
print(a.fib(0))