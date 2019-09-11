def isPowerOfFour(num):
    """
    :type num: int
    :rtype: bool
    """
    if num == 0:
        return False

    while num != 1:
        if num % 4 != 0:
            return False
        num = int(num/4)

    return True

print(isPowerOfFour(6))

"""
四的幂的2进制很有特点，从二进制入手
# 100
# 10000
# 1000000
# 100000000

    return (not(num&(num-1))) and (num>0) and ((num&0x55555555)==num)
"""

"""
与上面同理，上面与0x55555555就是确保1在奇数位
if (num & (num-1) == 0):  # Check if only has one 1
            while (num > 0):  # Check if the 1 is at even bit
                if (num == 1):
                    return True
                num >>= 2
        return False
"""