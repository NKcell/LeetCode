def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    flag = 0
    start = 0
    vlaues = []
    while flag < len(s):
        if s[flag] not in s[start:flag]:
            flag += 1
        else:
            vlaues.append(flag - start)
            start = s[start:flag].find(s[flag]) + 1 + start

    vlaues.append(flag - start)

    if len(vlaues) == 0:
        return 0
    else:
        return max(vlaues)

def lengthfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    d = {}
    start = 0
    maxlen = 0
    for i, c in enumerate(s):
        if (c not in d or d[c] < start):
            maxlen = max(maxlen, 1 + i - start)
        else:
            start = d[c] + 1
        d[c] = i
    return maxlen

print(lengthOfLongestSubstring("bpfbhmipx"))
print(lengthfLongestSubstring('babababaabaabcdf'))


