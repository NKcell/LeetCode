def solution(n: int) -> str:
        alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        res = list()
        while n > 0:
            mod = (n % 26)-1
            res.append(alphabet[mod])
            if n == 26:
                break
            n = n//26
            if mod == -1:
                n -= 1
        return ''.join(res[::-1])

class Solution:
    # 主要的就是理解这个-1
    def convertToTitle(self, num: int) -> str:
        return "" if num == 0 else self.convertToTitle((num - 1) / 26) + chr((num - 1) % 26 + ord('A'))