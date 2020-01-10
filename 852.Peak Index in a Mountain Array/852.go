package leetcode

func peakIndexInMountainArray(A []int) int {
    start := 0
	end := len(A)-1
	for start<=end{
		mid := (start+end)/2
		if A[mid]>A[mid-1] && A[mid]>A[mid+1]{
			return mid
		}
		if A[mid]>A[mid-1]{
			start = mid+1
		}else{
			end = mid-1
		}
	}
    return 0
}