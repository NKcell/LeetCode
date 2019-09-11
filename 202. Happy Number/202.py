"""
202. Happy Number
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example:

Input: 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""

def get_num(num):
    num = str(num)
    sum = 0
    for i in num:
        sum += int(i) ** 2
    return sum

def isHappy(n):
    """
    :type n: int
    :rtype: bool
"""
    re_list = [n]
    while True:
        if n == 1:
            return True
        n = get_num(n)
        if n in re_list:
            return False
        re_list.append(n)


print(isHappy(19))

"""
思想一样但更简洁
def isHappy(self, n):
    mem = set()
    while n != 1:
        n = sum([int(i) ** 2 for i in str(n)])
        if n in mem:
            return False
        else:
            mem.add(n)
    else:
        return True
"""

"""
这个判断是否会陷入无限循环的方式应该说节约内存，但这种判断方法细想一下感觉不是很有道理。。。
def isHappy(self, n):
    r1 = self.step(n)
    r2 = self.step(r1)
    while(r1 != 1):
        if(r1 == r2):
            return False
        else:
            r1 = self.step(r1)
            r2 = self.step(self.step(r2))
    return True

def step(self, n):
    result = 0
    while(n):
        result += pow(n % 10, 2)
        n = n // 10
    return result
"""