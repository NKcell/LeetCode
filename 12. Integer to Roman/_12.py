class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        while num != 0:
            if num>=1000:
                res += 'M'
                num -= 1000
                continue
            elif num >= 900:
                res += 'CM'
                num -= 900
                continue
            elif num>= 500:
                res += 'D'
                num -= 500
                continue
            elif num>=400:
                res += 'CD'
                num -= 400
                continue
            elif num >= 100:
                res += 'C'
                num -= 100
                continue
            elif num>= 90:
                res += 'XC'
                num -= 90
                continue
            elif num >= 50:
                res += 'L'
                num -= 50
                continue
            elif num>= 40:
                res += 'XL'
                num -= 40
                continue
            elif num>=10:
                res += 'X'
                num -= 10
                continue
            elif num >= 9:
                res += 'IX'
                num -= 9
                continue
            elif num>= 5:
                res += 'V'
                num -= 5
                continue
            elif num >= 4:
                res += 'IV'
                num -= 4
                continue
            elif num>= 1:
                res += 'I'
                num -= 1
                continue

        return res

a = Solution()
print(a.intToRoman(3))