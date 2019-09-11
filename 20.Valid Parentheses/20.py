def judge(l1,l2):
    if (l1 == '('and l2 == ')') or (l1 == '['and l2 == ']') or (l1 == '{'and l2 == '}'):
        return True
    else:
        return False

def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    k = []
    for i in range(len(s)):
        if s[i] in ['(','{','[']:
            k.append(s[i])
        else:
            if len(k) == 0:
                return False
            if judge(k[-1],s[i]):
                k.pop()
            else:
                return False
    if len(k) == 0:
        return True
    else:
        return False

print(isValid('()'))