package leetcode

func distributeCandies(candies []int) int {
	myDict := make(map[int]int, 0)
	for _, v := range candies{
		myDict[v]++
	}
	if len(myDict)<len(candies)/2{
		return len(myDict)
	}
	return len(candies)/2
}