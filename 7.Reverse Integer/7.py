def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    temp = 0
    if x == 0:
        return x

    elif x > 0:
        while True:
            if x//10 == 0 and x%10 == 0:
                break
            temp = temp*10 + x%10
            x = x//10
        if temp > 2147483647:
            return 0
        return  temp
    else:
        x = -x
        while True:
            if x//10 == 0 and x%10 == 0:
                break
            temp = temp*10 + x%10
            x = x//10
        if temp > 2147483648:
            return 0
        return -temp

t = input('请输入一个整数：')
print(reverse(int(t)))