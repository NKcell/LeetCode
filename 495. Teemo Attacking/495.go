package leetcode

func findPoisonedDuration(timeSeries []int, duration int) int {
    res := 0
	for i:=1; i<len(timeSeries); i++{
		if timeSeries[i-1]+duration < timeSeries[i]{
			res += duration
		}else{
			res += (timeSeries[i]-timeSeries[i-1])
		}
	}
	if len(timeSeries)>=1{
		res += duration
	}
	return res
}