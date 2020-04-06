package leetcode

func findLucky(arr []int) int {
	myDict := make(map[int]int, 0)
	
	for _,v := range arr{
		if value, ok := myDict[v]; ok{
			myDict[v] = (value+1)
		}else{
			myDict[v] = 1
		}
	}

	res := -1

	for i,v := range myDict{
		if i==v{
			if v>res{
				res = v
			}
		}
	}

	return res
}