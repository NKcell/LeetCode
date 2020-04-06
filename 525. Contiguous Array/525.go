package leetcode

func findMaxLength(nums []int) int {
    myDict := make(map[int]int, 0)
	count := 0
	maxLength := 0
	myDict[0] = 0

	for i,v := range nums{
		if v == 0{
			count --
		}else{
			count ++
		}

		i ++
		
		if tmp, ok := myDict[count];!ok{
			myDict[count] = i
		}else{
			if i-tmp > maxLength{
				maxLength = i-tmp
			}
		}
	}

	return maxLength
}