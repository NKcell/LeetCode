def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    l = 0
    flag = 0
    for i in range(len(s)):
        if s[len(s)-1-i] == ' 'and flag == 0:
            pass
        elif s[len(s)-1-i] != ' ':
            l += 1
            flag += 1
        elif s[len(s)-1-i] == ' 'and flag != 0:
            return l
    return l

print(lengthOfLastWord('e'))