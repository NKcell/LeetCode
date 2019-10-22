package leetcode

func repeatedNTimes(A []int) int {
	myDict := make(map[int]int, len(A)/2+1)
	for _, v := range A{
		_, ok := myDict[v]
		if ok{
			return v
		}
		myDict[v] = 1
	}
	return -1
}

// 这里用bool作为值类型，内存开销会减少，时间也更快
func repeatedNTimes1(A []int) int {
    seen := make(map[int]bool)
    
    for _, num := range A {
        if seen[num] {
            return num
        } 
        seen[num] = true
    }
    return -1
}