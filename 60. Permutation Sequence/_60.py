class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        import math
        tmp = list(range(1,n+1))
        res = ""
        while tmp:
            n -= 1
            if n == 0 :
                res += str(tmp[0])
                break
            chushu = math.factorial(n)
            index = k//chushu
            k = k%chushu
            if k == 0:
                index -= 1
            res += str(tmp[index])
            del tmp[index]
            
        return res

    def getPermutation1(self, n, k):
        import math
        numbers = list(range(1, n+1))
        permutation = ''
        k -= 1
        while n > 0:
            n -= 1
            # get the index of current digit
            index, k = divmod(k, math.factorial(n))
            permutation += str(numbers[index])
            # remove handled number
            numbers.remove(numbers[index])

        return permutation

a = Solution()
print(a.getPermutation1(n = 3, k = 2))