"""
264. Ugly Number II

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:

1 is typically treated as an ugly number.
n does not exceed 1690.
"""


# 不用想了肯定超时的代码
"""
def nthUglyNumber(n):

    count = 0
    flag = 1

    while count<n:
        if isUgly(flag):
            count += 1
            #print(flag)
        flag += 1

    return flag-1


def isUgly(num):

    if num < 1:
        return False

    while num != 1:
        if num % 2 != 0 and num % 3 != 0 and num % 5 != 0:
            return False
        if num % 2 == 0:
            num = num // 2
        if num % 3 == 0:
            num = num // 3
        if num % 5 == 0:
            num = num // 5
    return True
"""
def nthUglyNumber(n):
    my_2 = 0
    my_3 = 0
    my_5 = 0

    ugly = [1]

    while n>1:
        u2,u3, u5 = ugly[my_2]*2, ugly[my_3]*3, ugly[my_5]*5
        u_min = min(u2,u3,u5)
        if u2 == u_min:
            my_2 += 1
        if u3 == u_min:
            my_3 += 1
        if u5 == u_min:
            my_5 += 1
        ugly.append(u_min)
        n -= 1

    return ugly[-1]


print(nthUglyNumber(1690))

# 这种暴力的反而快？
"""
class Solution:
    ugly = sorted(2**a * 3**b * 5**c
                  for a in range(32) for b in range(20) for c in range(14))
    def nthUglyNumber(self, n):
        return self.ugly[n-1]
"""
















