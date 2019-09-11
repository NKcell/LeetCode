def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """

    values = 0
    for i in digits:
        values = values*10 + i

    values += 1

    l = []
    while values//10 != 0:
        l.append(values%10)
        values = values//10

    l.append(values)

    l.reverse()
    return l

print(plusOne([0]))