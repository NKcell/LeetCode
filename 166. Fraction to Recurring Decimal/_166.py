def solution(numerator: int , denominator: int) -> str:
        res = list()

        if numerator*denominator<0:
            res.append("-")

        numerator = abs(numerator)
        denominator = abs(denominator)

        if numerator<denominator:
            res.append('0')

        while numerator>=denominator:
            mod = numerator%denominator
            res.append(str(numerator//denominator))
            numerator = mod

        if numerator == 0:
            return ''.join(res)
        else:
            res.append('.')

        mydict = {}
        numerator = numerator*10
        mydict[numerator] = len(res)
        while numerator != 0:
            mod = numerator%denominator
            res.append(str(numerator//denominator))
            numerator = mod*10
            ok = mydict.get(numerator, -1)
            if ok != -1:
                res = res[:ok] + ['('] + res[ok:] + [')']
                return ''.join(res)
            else:
                mydict[numerator] = len(res)

        return ''.join(res)

# python 自带的divmod函数有意思， 通过replace， rstrip等函数来实现减少判断
def fractionToDecimal1(self, numerator, denominator):
    n, remainder = divmod(abs(numerator), abs(denominator))
    sign = '-' if numerator*denominator < 0 else ''
    result = [sign+str(n), '.']
    stack = []
    while remainder not in stack:
        stack.append(remainder)
        n, remainder = divmod(remainder*10, abs(denominator))
        result.append(str(n))

    idx = stack.index(remainder)
    result.insert(idx+2, '(')
    result.append(')')
    return ''.join(result).replace('(0)', '').rstrip('.')

# 这个和我的方法类似，但思路清晰很多
def fractionToDecimal2(self, numerator, denominator):
    num, den = numerator, denominator
    if not den:  # denominator is 0
        return 
    if not num:  # numerator is 0
        return "0"
    res = []
    if (num < 0) ^ (den < 0):
        res.append("-")  # add the sign
    num, den = abs(num), abs(den)
    res.append(str(num//den))
    rmd = num % den
    if not rmd:
        return "".join(res)  # only has integral part
    res.append(".")  # has frational part
    dic = {}
    while rmd:
        if rmd in dic:   # the remainder recurs
            res.insert(dic[rmd], "(")
            res.append(")")
            break
        dic[rmd] = len(res) 
        div, rmd = divmod(rmd*10, den)
        res.append(str(div))
    return "".join(res)