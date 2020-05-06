package leetcode

func minStartValue(nums []int) int {
	res := 0
	tmp := 0

	for _, v := range nums{
		tmp += v
		if tmp<res{
			res = tmp
		}
	}

	return (res-1)*-1
}