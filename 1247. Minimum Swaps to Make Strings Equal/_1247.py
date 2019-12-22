class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        res = list()
        for i,v in enumerate(s1):
            if v != s2[i]:
                res.append(v)

        if len(res)%2 != 0:
            return -1
        
        x = res.count('x')
        y = res.count('y')

        if x%2 != 0:
            return x//2+y//2+2
        else:
            return x//2+y//2

    def minimumSwap1(self, s1, s2):
        x1 = 0
        y1 = 0
        for i in range(len(s1)):
            if s1[i] != s2[i] and s1[i] == "x":
                x1 += 1
            if s1[i] != s2[i] and s1[i] == "y":
                y1 += 1
        if (x1 + y1) % 2 != 0:
            return -1
        return x1 / 2 + y1 / 2 + 2 * (x1 % 2)

    def minimumSwap2(self, s1: str, s2: str, xy: int = 0, yx: int = 0) -> int:
        for a, b in zip(s1, s2):
            xy += a == 'x' and b == 'y'
            yx += a == 'y' and b == 'x'
        return xy // 2 + xy % 2 + yx // 2 + yx % 2 if xy % 2 == yx % 2 else -1

a = Solution()
print(a.minimumSwap(s1 = "xxyyxyxyxx", s2 = "xyyxyxxxyx"))