class Solution:
    def maximum69Number (self, num: int) -> int:
        tmp = list(str(num))
        for i,v in enumerate(tmp):
            if v == '6':
                tmp[i] = '9'
                return int(''.join(tmp))
        return num