def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str


    看错题目，需要判断的仅仅是前缀
    temp = ''
    flag = 1
    for i in range(len(strs)):
        j = 0

        while i + j + 1 < (len(strs)+1):
            flag = 1
            # print(strs[0][j:i+j+1])
            for o in strs:
                if o.find(strs[0][j:i+j+1]) < 0:
                    flag = 0
                    break
            if flag == 1:
                temp = strs[0][j:i+j+1]
                break
            j += 1
        if flag == 0:
            return temp

    return  temp
"""
    temp = ''
    if len(strs) == 0:
        return  temp
    if '' in strs:
        return  temp
    if len(strs) == 1:
        return strs[0]
    least_str = strs[0]
    for i in strs:
        if len(least_str) > len(i):
            least_str = i

    for i in range(len(least_str)):
        for j in strs:
            if i == 0:
                if least_str[0:1] != j[0:1]:
                    return temp
            else:
                if least_str[0:i+1] != j[0:i+1]:
                    return temp
        if i == 0:
            temp = least_str[0]
        else:
            temp = least_str[0:i+1]
    return temp

print(longestCommonPrefix(["aa","aa"]))
print(longestCommonPrefix(["aa","ab"]))
print(range(1))

