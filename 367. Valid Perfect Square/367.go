package leetcode

func isPerfectSquare(num int) bool {
	start := 1
	end := num
	for(start <= end){
		mid := (start+end)/2
		tmp := mid*mid
		if tmp == num{
			return true
		}
		if tmp>num{
			end = mid-1
		}else{
			start = mid+1
		}
	}

	return false
}