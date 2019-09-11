def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 1:
        step = 1
        return step
    if n == 2:
        step = 2
        return step

    f = 1
    l = 2
    i = 2
    while i < n:
        temp = f + l
        f = l
        l = temp
        i += 1
    return temp


print(climbStairs(35))