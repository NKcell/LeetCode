package leetcode

func minTimeToVisitAllPoints(points [][]int) int {
	res := 0
	for i:=1; i<len(points); i++{
		res += max(abs(points[i][0]-points[i-1][0]),abs(points[i][1]-points[i-1][1]))
	}
	return res
}

func abs(value int) int{
	if value<0{
		return -value
	}
	return value
}

func max(a, b int) int{
	if a>b{
		return a
	}
	return b
}