package leetcode

func groupThePeople(groupSizes []int) [][]int {
	myDict := make(map[int][]int, 0)
	
	for i,v := range groupSizes{
		if tmplist,ok := myDict[v]; ok{
			tmplist = append(tmplist, i)
			myDict[v] = tmplist
		}else{
			tmplist := make([]int, 0, 1)
			tmplist = append(tmplist, i)
			myDict[v] = tmplist
		}
	}

	res := make([][]int, 0)
	for i,v := range myDict{
		start := 0
		for start<len(v){
			if start+i<=len(v){
				res = append(res, v[start: start+i])
			}else{
				res = append(res, v[start: len(v)])
			}
			start += i
		}
	}

	return res
}									