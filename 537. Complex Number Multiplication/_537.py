class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        a1,a2 = a.split('+')
        b1,b2 = b.split('+')

        a1,a2,b1,b2 = int(a1), int(a2.split('i')[0]), int(b1), int(b2.split('i')[0])

        res1 = a1*b1 - a2*b2
        res2 = a1*b2 + a2*b1

        return str(res1) + '+' + str(res2) + 'i'

    def complexNumberMultiply1(self, a, b):
        a1, a2 = map(int, a[:-1].split('+'))
        b1, b2 = map(int, b[:-1].split('+'))
        return '%d+%di' % (a1 * b1 - a2 * b2, a1 * b2 + a2 * b1)

a = Solution()
print(a.complexNumberMultiply1("1+1i", "1+1i"))