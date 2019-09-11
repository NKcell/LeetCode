def magicalString(n):
    """
    :type n: int
    :rtype: int
    """
    s =  "1221121221221121122"
    if n < len(s):
        return s[0:n].count('1')

    return(judge(s, n)[0:n].count('1'))


def judge(s, n):
    pin = []
    flag = 0
    for i in range(len(s)):
        if flag == 1:
            flag = 0
            continue
        if s[i] == s[i + 1]:
            pin.append('2')
            flag = 1
        else:
            pin.append('1')

    temp = len(pin)
    while True:
        if s[temp] == '1':
            if s[-1] == '1':
                s += '2'
            else:
                s += '1'
        else:
            if s[-1] == '1':
                s += '22'
            else:
                s += '11'

        if len(s) >= n:
            break
        temp += 1

    return s

print(magicalString(30))

"""
def magicalString(self, n):

        :type n: int
        :rtype: int

        nums = [1, 2, 2]
        i = 2
        while len(nums) < n:
            nums.append(3 - nums[-1])
            if nums[i] == 2:
                nums.append(nums[-1])
            i += 1
        
        count = 0
        for i in range(n):
            if nums[i] == 1:
                count += 1
        return count
        
def magicalString(self, n):
    cnt, s, two = 0, "1", True
    for i in range(n - 1):
        if s[i] == "1":
            cnt += 1
            s += two and "2" or "1"
        else: s += two and "22" or "11"
        two = not two
    return cnt if n != 1 else 1
"""