class Solution:
    def numberOfSteps (self, num: int) -> int:
        count = 0
        while num!=0:
            if num%2 == 1:
                num-=1
            else:
                num /= 2
            count += 1
        return count

    def numberOfSteps1 (self, num: int) -> int:
        digits = f'{num:b}'
        return digits.count('1') - 1 + len(digits)

    