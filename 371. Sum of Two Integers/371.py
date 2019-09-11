"""
371. Sum of Two Integers
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -
"""


def getSum(a, b):
    """
    :type a: int
    :type b: int
    :rtype: int
    """
    if a<0:
        a = bin(a)[3:]
        flaga = 1
    else:
        a = bin(a)[2:]
        flaga = 0

    if b<0:
        b = bin(b)[3:]
        flagb = 1
    else:
        b = bin(b)[2:]
        flagb = 0

    if flaga == flagb:
        jw = 0
        res = ''

        while (a != '' and b!='') or (jw ==1):
            try:
                inta = int(a[-1])
            except:
                inta = 0

            try:
                intb = int(b[-1])
            except:
                intb = 0

            res = str(inta ^ intb ^jw) + res
            a = a[:-1]
            b = b[:-1]
            if [inta, intb, jw].count(1) >= 2:
                jw = 1
            else:
                jw = 0

        res = a + b + res
        if flaga == 1:
            return int('-'+res,2)
        else:
            return int(res,2)

    else:
        if flagb==1:
            if int(a) > abs(int(b)):
                return int(zf(a,b),2)
            else:
                return int('-' + zf(b,a),2)

        else:
            if int(b) > abs(int(a)):
                return int(zf(b, a), 2)
            else:
                return int('-' + zf(a, b), 2)


def zf(a,b):
    jw = 0
    res = ''
    while (a != '' or b != '') :
        try:
            inta = int(a[-1])
        except:
            inta = 0

        try:
            intb = int(b[-1])
        except:
            intb = 0

        a = a[:-1]
        b = b[:-1]

        if inta == intb:
            if jw == 1:
                res = '1' + res
                jw = 1
            else:
                res = '0' + res
                jw = 0
        else:
            if inta == 1:
                if jw == 1:
                    res = '0' + res
                    jw = 0
                else:
                    res = '1' + res
                    jw = 0
            else:
                if jw == 1:
                    res = '0' + res
                    jw = 1
                else:
                    res = '1' + res
                    jw = 1
    return res


print (getSum(20,-40))

"""
def getSum(self, a, b):
      
        :type a: int
        :type b: int
        :rtype: int
       
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        while b != 0:
            # ^ get different bits and & gets double 1s, << moves carry
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        return a if a <= MAX else ~(a ^ mask)
"""