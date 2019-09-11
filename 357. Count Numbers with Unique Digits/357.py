"""
357. Count Numbers with Unique Digits
Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:

Input: 2
Output: 91
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100,
             excluding 11,22,33,44,55,66,77,88,99
"""


def countNumbersWithUniqueDigits(n):
    """
    :type n: int
    :rtype: int
    """
    if n>10:
        n = 10

    val = 1

    flag = 0
    while flag < n:
        flag += 1
        temp = flag
        val1 = 1
        val2 = 10
        while temp > 0:
            val1 = val1*val2
            val2 -= 1
            temp -= 1

        val1 = val1*0.9

        val = val + val1

    return int(val)

print(countNumbersWithUniqueDigits(3))

"""
    def countNumbersWithUniqueDigits(self, n):
        # n can not be greater than 10 as it must exist two of the digit share same number
        # f(n) = 1-digits unique num combination + 2-digits unique num combination + ...
        # f(n) = 10 + 9 * 9 + 9 * 9 * 8 + ...
        # f(n) = g(0) + g(1) + g(2) + ... + g(n)
        # g(0) = 10
        # g(1) = 9 * 9
        # g(2) = 9 * 9 * 8
        # g(k) = 9 * (10 - 1) * (10 - 2) * ... * (10 - k)
        if n == 0: return 1
        if n == 1: return 10
        n = min(10, n)
        res = 10
        for n in range(1, n):
            g = 9
            for i in range(1, n+1):
                g *= (10 - i)
            res += g
        return res
"""