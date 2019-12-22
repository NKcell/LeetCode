package leetcode

func searchMatrix(matrix [][]int, target int) bool {
	if len(matrix) == 0 || len(matrix[0]) == 0{
		return false
	}
	start, end, flag, mindex := 0, len(matrix)-1, 0, 0
	for start<=end{
		mid := (start+end)/2
		if matrix[mid][0]>target{
			end=mid-1
		}else if matrix[mid][len(matrix[0])-1]<target{
			start=mid+1
		}else{
			flag = 1
			mindex = mid
			break
		}
	}
	if flag == 0{
		return false
	}

	start, end = 0, len(matrix[0])-1
	for start<=end{
		mid := (start+end)/2
		if matrix[mindex][mid]>target{
			end=mid-1
		}else if matrix[mindex][mid]<target{
			start=mid+1
		}else{
			flag = 0
			break
		}
	}
	if flag == 1{
		return false
	}
	return true
}