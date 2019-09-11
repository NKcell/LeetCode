"""
326
Given an integer, write a function to determine if it is a power of three.
Could you do it without using any loop / recursion?
"""
def isPowerOfThree(n):
    """
    :type n: int
    :rtype: bool
    """
    if n <= 0:
        return False

    while n != 1:
        if n % 3 != 0:
            return False
        n = n/3

    return True

print(isPowerOfThree(1))

"""
    def isPowerOfThree(self, n):

        :type n: int
        :rtype: bool

        # 3^x = n -> x = log_3(n) = log(n)/log(3)
        if n <= 0:
            return False
        elif n == 1:
            return True
        import math
        x = math.log(n) / math.log(3)
        return 3 ** int(round(x)) == n
"""