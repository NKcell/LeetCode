def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    temp = 0
    for i in range(len(s)):
        if i+1 < len(s):
            if dic[s[i]] >= dic[s[i+1]]:
                temp += dic[s[i]]
            else:
                temp -= dic[s[i]]
        else:
            temp += dic[s[i]]
    return  temp

roman = input('请输入罗马数字：')
print(romanToInt(roman))