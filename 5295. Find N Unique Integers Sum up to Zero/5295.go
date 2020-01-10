package leetcode

func sumZero(n int) []int {
	res := make([]int, 0, n)
	if n%2 == 1{
		res = append(res, 0)
		n --
	}

	for n!=0{
		res = append(res, n, -n)
		n -= 2
	}

	return res
}