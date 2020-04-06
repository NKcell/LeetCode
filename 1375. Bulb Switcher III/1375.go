package leetcode

func numTimesAllBlue(light []int) int {
    maxNum := 1
	count := 0

	for i,v := range light{
		if v>maxNum{
			maxNum = v
		}

        if (i+1)>=maxNum{
			count ++
		}
	}

	return count
}