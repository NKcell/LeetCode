def countAndSay(n):
    """
    :type n: int
    :rtype: str
    """
    i = '1'
    if n == 1:
        return i
    flag = 1
    while flag < n:
        num = 1
        s = ''
        for j in range(len(i)):
            if j+1 < len(i):
                if i[j] == i[j+1]:
                    num += 1
                else:
                    s += (str(num) + str(i[j]))
                    num = 1
            else:
                    s += (str(num) + str(i[j]))
        i = s
        flag += 1

    return s

print(countAndSay(1))