"""

超时
def countPrimes(n):
        if n < 3:
            return 0
        if n == 3:
            return 1

        primes = [2]
        re = 1

        for i in range(2,n):
            flag = 0
            for j in primes:
                if i%j == 0:
                    flag = 1
                    break
            if flag == 0:
                re += 1
                primes.append(i)

        return re
"""


def countPrimes(n):
    primes = [True]*n
    if n < 3:
        return 0
    primes[0] = False
    primes[1] = False

    for i in range(2,int(n**0.5) + 1):
        if primes[i]:
            for j in range(i*i,n,i):
                primes[j] = False

    return sum(primes)



print(countPrimes(3))

"""
class Solution:
# @param {integer} n
# @return {integer}
def countPrimes(self, n):
    if n < 3:
        return 0
    primes = [True] * n
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
    return sum(primes)
"""