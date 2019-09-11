def selfDividingNumbers(left, right):
    """
    :type left: int
    :type right: int
    :rtype: List[int]
    """
    fin = []
    for i in range(left, right+1):
        if  '0' in str(i):
            continue

        temp = i
        nums = []
        while True:
            nums.append(temp%10)
            temp = temp//10
            if temp == 0:
                break

        flag = 0
        for j in nums:
            if i%j != 0:
                flag = 1
                break
        if flag == 0:
            fin.append(i)
    return fin

print(selfDividingNumbers(1,22))