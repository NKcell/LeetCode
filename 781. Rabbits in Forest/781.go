package leetcode

func numRabbits(answers []int) int {
    myDict := make(map[int]int, 0)
	for _,v := range answers{
		myDict[v]++;
	}

	count := 0
	for i,v := range myDict{
		if v%(i+1) == 0{
			count += v
		}else{
			count += (v/(i+1)+1)*(i+1)
		}
	}
	return count
}