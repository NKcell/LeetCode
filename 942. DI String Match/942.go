package leetcode

func diStringMatch(S string) []int {
	res := make([]int, len(S)+1)
	min := 0
	max := 0
	for i,v := range S{
		if v == 'I'{
			max ++
			res[i+1] = max
		}else{
			min --
			res[i+1] = min
		}
	}

	for i,v := range res{
		res[i] = v-min
	}

	return res
}