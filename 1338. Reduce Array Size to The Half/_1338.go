package leetcode

func minSetSize(arr []int) int {
    halfLen := (len(arr)+1)/2
	myDict := make(map[int]int, 0)
	for _,v := range arr{
		myDict[v]++
	}

	count := 0
	value := 0

	res := make([]int, 0, len(myDict))
	for _,v := range myDict{
		res = append(res, v)
	}

	sort.Ints(res)

	for i:=len(res)-1; i>=0; i--{
		value += res[i]
		count++
		if value >= halfLen{
			return count
		}
	}
	return count
}