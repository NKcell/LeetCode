package leetcode

func uniqueOccurrences(arr []int) bool {
	myDict := make(map[int]int, 0)
	for _, v := range arr{
		myDict[v]++
	}
	myDict2 := make(map[int]int,len(myDict))
	for _,v := range myDict2{
		myDict2[v] ++
	}
	for _, v := range myDict2{
		if v != 1{
			return false
		}
	}
	return true
}

//上面代码可以优化，判断退出写在第二个循环里就好了
func uniqueOccurrences1(arr []int) bool {
    
    tmp := make(map[int]int)
    temp := make(map[int]int)
    
    for _, v := range arr {
        tmp[v]++
    }
    for _, v := range tmp {
        temp[v]++
        if temp[v] > 1 { return false }
    }
    return true
}