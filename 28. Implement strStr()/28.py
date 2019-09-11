def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    # return (haystack.find(needle))

    if len(needle) == 0:
        return 0
    head = []
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i] == needle[0]:
            head.append(i)
    if len(head) == 0:
        return -1

    for i in head:
        if haystack[i:i+len(needle)] == needle:
            return i

    return -1