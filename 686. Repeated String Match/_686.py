class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        flag = 1
        while flag*len(A)<len(B):
            flag += 1
        if B in (flag*A):
            return flag
        flag += 1
        if B in (flag*A):
            return flag
        return -1

    def repeatedStringMatch1(self, A, B):
        t = -(-len(B) // len(A)) # Equal to ceil(len(b) / len(a))
        return t * (B in A * t) or (t + 1) * (B in A * (t + 1)) or -1

a = Solution()
print(a.repeatedStringMatch(A = "abab" , B = "aba"))