def myAtoi(str):
    """
    :type str: str
    :rtype: int
    
    if str == '':
        return 0

    flag = 0
    for i in range(len(str)):
        if str[i] == ' ':
            flag += 1
            if i == len(str)-1:
                return 0
        else:
            break

    if str[flag] != '+' and str[flag] != '-' and (not str[flag].isdigit()):
        return 0

    if ((str[flag] == '+' or str[flag] == '-') and flag == len(str)-1) or ((str[flag] == '+' or str[flag] == '-') and (not str[flag+1].isdigit())):
        return 0

    #print(str[flag])
    tem = flag
    if str[flag] != '+' and str[flag] != '-':
        while tem < len(str):
            if str[tem].isdigit():
                tem += 1
            else:
                break

        res = str[flag:tem]
        res = int(res)
        if res > 2**31-1:
            return 2**31-1
        else:
            return res

    else:
        print(1)
        tem = flag + 1
        while tem < len(str):
            if str[tem].isdigit():
                tem += 1
            else:
                break

        res = str[flag+1:tem]
        res = int(res)
        if str[flag] == '+':
            if res > 2 ** 31 - 1:
                return 2 ** 31 - 1
            else:
                return res
        else:
            if res > 2** 31:
                return -2**31
            else:
                return -res
                """


def myAtoi(s):
    s = s.strip()
    try:
        val = ''
        for i in range(len(s)):
            if (s[i] in '+-' and i == 0) or '0' <= s[i] <= '9':
                val += s[i]
            else: break
        val = int(val)
        if val < -2**31: return -2**31
        if val > 2**31-1: return 2**31-1
        return val
    except:
        return 0


print(myAtoi('   kkk'))