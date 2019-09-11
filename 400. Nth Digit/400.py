def findNthDigit(n):
    """
    :type n: int
    :rtype: int
    """
    count = 1

    flag = 9
    while n > flag:
        count += 1
        flag += 9*(10**(count-1))*count

    num = (n - flag + 9*(10**(count-1))*count-1)//count
    #print (num)
    juti = num + (10**(count-1))
    #print (juti)
    num2 = (n-flag-1)%count

    return int(str(juti)[num2])



print(findNthDigit(3))