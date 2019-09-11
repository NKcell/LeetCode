def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0:
        return False

    temp = int(str(x)[::-1])
    if temp == x:
        return True
    else:
        return False

x = input('请输入一个整数：')
print(isPalindrome(int(x)))


def two(x):
    num = x
    if (x < 0):
        return False

    res = 0
    while (x > 0):
        res = res * 10
        res = res + x % 10
        x = x // 10
    return (num == res)