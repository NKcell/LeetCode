package leetcode

func singleNumber(nums []int) int {
	myDict := make(map[int]int)
    for _,v := range nums{
		_, ok := myDict[v]
		if !ok{
			myDict[v] = 1
		}else{
			delete(myDict, v)
		}
	}
	for i := range myDict{
		return i
	}
	return 0
}

// 异或快很多，这种题要多思考异或的方法
func singleNumber1(nums []int) int {
    result := 0
    for _,v := range nums{
        result = result ^ v
    }
    return result
}