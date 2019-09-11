def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    ans = []
    l = len(s)
    flag = 0
    for i in range(l-1):
        j = l
        if j - i < flag:
            break
        while j > i+1:
            if s[i:j] == s[i:j][::-1]:
                ans.append(s[i:j])
                if flag < len(s[i:j]):
                    flag = len(s[i:j])
                break
            else:
                j -= 1

    if s == '':
        return ''
    if len(ans) == 0:
        return s[0]
    else:
        return(list(sorted(ans, key = lambda x: len(x), reverse = True))[0])

print(longestPalindrome("abacab"))