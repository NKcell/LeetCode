def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    minnum = 0
    if x == 1:
        return 1
    maxnum = x

    while minnum != maxnum and minnum != maxnum - 1:
        mid = (minnum + maxnum) // 2
        if mid ** 2 == x:
            return mid
        elif mid ** 2 > x:
            maxnum = mid
        else:
            minnum = mid

    return minnum

print(mySqrt(6))