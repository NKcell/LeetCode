class Solution:
    def peakIndexInMountainArray(self, A:) -> int:
        start = 0
        end = len(A)-1
        while start<=end:
            mid = (start+end)//2
            if A[mid]>A[mid-1] and A[mid]>A[mid+1]:
                return mid
            if A[mid]>A[mid-1]:
                start = mid+1
            else:
                end = mid-1