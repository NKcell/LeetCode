def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """

    if numRows == 1:
        return s

    s_length = len(s)
    flag = []

    for i in range(s_length):
        tem = i%(2*numRows-2)
        if tem < numRows:
            flag.append(tem)
        else:
            flag.append(2*numRows-2-tem)

    fin = ''

    for i in range(numRows):
        for j in range(s_length):
            if flag[j] == i:
                fin = fin + s[j]

    return fin



print(convert('PAYPALISHIRING',4))

