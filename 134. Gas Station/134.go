package leetcode

func canCompleteCircuit(gas []int, cost []int) int {
    if mysum(gas) < mysum(cost){
		return -1
	}

	start := 0
	remain := 0
	for i,v := range gas{
		remain += (v-cost[i])
		if remain<0{
			start = i+1
			remain = 0
		}
	}

	return start
}

func mysum(tmp []int) int{
	res := 0
	for _,v := range tmp{
		res += v
	}
	return res
}