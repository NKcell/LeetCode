package leetcode

func findRestaurant(list1 []string, list2 []string) []string {
	myDict := make(map[string]int, len(list1))
	myDict1 := make(map[string]int, len(list2))
	for i, v := range list1{
		myDict[v] = i
	}
	for i, v := range list2{
		dictv, ok := myDict[v]
		if ok{
			myDict1[v] = i+dictv
		}
	}
	minValue := 2000
	res := make([]string, 0)
	for i, v := range myDict1{
		if v<minValue{
			res = []string{i}
			minValue = v
		}else if v == minValue{
			res = append(res, i)
		}
	}
	return res
}