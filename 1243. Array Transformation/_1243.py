class Solution:
    def transformArray(self, arr):
        while True:
            tmplist = [0]*len(arr)
            
            for i in range(1,len(arr)-1):
                if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
                    tmplist[i] = -1
                elif arr[i]<arr[i-1] and arr[i]<arr[i+1]:
                    tmplist[i] = 1

            if len(set(tmplist)) == 1:
                return arr
            else:
                for i,v in enumerate(arr):
                    arr[i] = v+tmplist[i]

    def transformArray1(self, A):
        for _ in range(100):
            A = A[:1] + [b + (a > b < c) - (a < b > c) for a, b, c in zip(A, A[1:], A[2:])] + A[-1:]
        return A

a = Solution()
print(a.transformArray([1,6,3,4,3,5]))