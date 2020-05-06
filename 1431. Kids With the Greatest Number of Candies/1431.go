package leetcode

func kidsWithCandies(candies []int, extraCandies int) []bool {
	maxNum := getMax(candies)
	res := make([]bool, 0, len(candies))
	for _,v := range candies{
		if v+extraCandies>=maxNum{
			res = append(res, true)
		}else{
			res = append(res, false)
		}
	}
	return res
}

func getMax(candies []int) int{
	res := candies[0]
	for _,v := range candies{
		if v > res{
			res = v
		}
	}
	return res
}