"""
201
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.
"""

"""
def rangeBitwiseAnd(m, n):

    z_list = set()
    for i in range(m, n + 1):
        for j in range(len(bin(i)) - 2):
            if bin(i)[2:][::-1][j] == '0':
                z_list.add(j)

    re = list(bin(i)[2:][::-1])
    for i in z_list:
        re[i] = '0'

    re = ''.join(re)[::-1]

    return int(re, 2)
"""
def rangeBitwiseAnd(m, n):
    s = m
    if m == n:
        return m

    temp = len(bin(m)[2:])*'0'
    temp = '1' +temp
    if int(temp,2) < n:
        return 0  # 比如100 10

    for i in range(m+1, n+1):
        s = s&i
        if s == 0:
            return s
    return s


print (rangeBitwiseAnd(600000000,2147483645))


"""
    def rangeBitwiseAnd(self, m, n):
        length = (m ^ n).bit_length() 
        n >>= length
        return n << length
"""


"""
def rangeBitwiseAnd(self, m, n):

        ret, num = m, m+1
        while num <= n:
            ret &= num
            count = 0
            while num % 2 == 0 and num != 0:
                count += 1
                num = num >> 1
            num += 1
            num = num << count
                
        return ret
"""

"""
i = 0
        while(n!=m):
            n = n>>1
            m = m>>1
            i+=1
        return n<<i
"""