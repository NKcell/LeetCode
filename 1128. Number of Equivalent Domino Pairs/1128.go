package leetcode

func numEquivDominoPairs(dominoes [][]int) int {
	var count int

	mymap := make(map[int]int, len(dominoes))
	for _, v := range dominoes{
		tmp1 := v[0]*10+v[1]
		tmp2 := v[1]*10+v[0]

		v1, ok1 := mymap[tmp1]
		v2, ok2 := mymap[tmp2]

		if !ok1 && !ok2{
			mymap[tmp1] = 1
		} else if ok1{
			mymap[tmp1] = v1+1
		}else{
			mymap[tmp2] = v2+1
		}
	}

	for i := range mymap{
		count += mymap[i]*(mymap[i]-1)/2
	}

	return count
}

// 这个还是使用的切片而不是字典，充分利用来只有两个数每个数不大于9这一条件
// 测试的是这个没有内存申请而上面的有两次，这个快来很多
func numEquivDominoPairs1(dominoes [][]int) int {
	res := 0
	count := [100]int{}
	for _, domino := range dominoes {
		d := mapping(domino)
		res += count[d]
		count[d]++
	}
	return res
}

func mapping(A []int) int {
	a, b := A[0], A[1]
	if a < b {
		return a*10 + b
	}
	return b*10 + a
}