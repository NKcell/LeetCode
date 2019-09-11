class Solution:
    def validMountainArray(self, A: list) -> bool:
        if len(A)<3:
            return False

        start = A[0]
        flag = 1
        if A[0]>A[1]:
            return False
        for i in range(1, len(A)):
            if start == A[i]:
                return False
            
            if start<A[i] and flag == 2:
                return False
            if start>A[i] and flag == 1:
                flag = 2
            start = A[i]
        
        if flag == 2:
            return True
        else:
            return False

    def validMountainArray1(self, A):
        i, j, n = 0, len(A) - 1, len(A)
        while i + 1 < n and A[i] < A[i + 1]: i += 1
        while j > 0 and A[j - 1] > A[j]: j -= 1
        return 0 < i == j < n - 1

    # 这个方法还是好理解，但感觉时间复杂度很高
    def validMountainArray2(self, A):
        if len(A)<3 or A == sorted(set(A)) or A[::-1] == sorted(set(A)):
            return False

        l = A.index(max(A))+1

        return A[:l] == sorted(set(A[:l])) and A[l-1:][::-1] == sorted(set(A[l-1:]))

a = Solution()
print(a.validMountainArray([2,1,2,3,5,7,9,10,12,14,15,16,18,14,13]))