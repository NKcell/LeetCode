package leetcode

func subtractProductAndSum(n int) int {
	sum := 0
	pro := 1
	for n!=0{
		tmp := n%10
		sum += tmp
		pro *= tmp
		n = n/10
	}
	return pro-sum
}
