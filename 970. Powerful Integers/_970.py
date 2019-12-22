class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) :
        res = set()
        i = 0
        if x == 1:
            x, y = y, x
        while x**i<bound:
            j = 0
            while x**i+y**j<=bound:
                res.add(x**i+y**j)
                j+=1
                if y == 1:
                    break
            i+=1
            if x == 1:
                break
        return list(res)

    def powerfulIntegers1(self, x, y, bound):
        xs = {x**i for i in range(20) if x**i < bound}
        ys = {y**i for i in range(20) if y**i < bound}
        return list({i + j for i in xs for j in ys if i + j <= bound})

a = Solution()
print(a.powerfulIntegers(x = 1, y = 2, bound = 10))