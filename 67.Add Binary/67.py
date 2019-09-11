def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    
    a = int(a, 2)
    b = int(b, 2)
    l = a+b
    return str(bin(l))[2:]
    """

    al = len(a)
    bl = len(b)
    flag = 0
    res = ''

    while al > 0 and bl > 0:
        if a[al-1] == '0' and b[bl-1] == '0' and flag == 0:
            res = '0' + res
        elif (a[al-1] == '0' and b[bl-1] == '0') or (a[al-1] == '0' and flag == 0) or (b[bl-1] == '0' and flag == 0):
            res = '1' + res
            flag = 0
        elif (a[al-1] == '1' and b[bl-1] == '1' and flag == 1):
            res = '1' + res
            flag = 1
        else:
            res = '0' + res
            flag = 1

        al -= 1
        bl -= 1

    if flag == 0:
        return (a[:al] + b[:bl] + res)
    else:
        if len(a[:al]) != 0:
            return (addBinary(a[:al], '1')+res)
        elif len(b[:bl]) != 0:
            return (addBinary(b[:bl], '1') + res)
        else:
            return ('1'+res)

print(addBinary('1','1'))