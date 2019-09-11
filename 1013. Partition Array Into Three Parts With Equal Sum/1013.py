class Solution:
    def canThreePartsEqualSum(self, A) -> bool:
        sumvalue = sum(A)

        if sumvalue%3 != 0:
            return False
        
        partvalue = sumvalue/3

        tmpvalue = 0
        tmpindex = 0
        flag = 0
        for i, v in enumerate(A):
            tmpvalue += v
            if tmpvalue == partvalue:
                flag += 1
                tmpindex = i
                tmpvalue = 0
            
            if flag == 2 and tmpindex != len(A)-1:
                return True
        return False

    # 思路一样这个写的更简洁吧
    def canThreePartsEqualSum1(self, A) -> bool:
        s, S, j = sum(A)//3, 0, 1
        for i in range(len(A)):
            S += A[i]
            if S == s:
                if j == 0: return True
                S = j = 0

a = Solution()
print(a.canThreePartsEqualSum([3,3,6,5,-2,2,5,1,-9,4]))