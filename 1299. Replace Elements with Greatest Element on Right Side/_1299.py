class Solution:
    def replaceElements(self, arr) :
        maxnum = -1
        for i in range(len(arr)-1, -1, -1):
            tmp = arr[i]
            arr[i] = maxnum
            maxnum = max(tmp, maxnum)
        return arr

    def replaceElements1(self, A, mx = -1):
        for i in range(len(A) - 1, -1, -1):
            A[i], mx = mx, max(mx, A[i])
        return A