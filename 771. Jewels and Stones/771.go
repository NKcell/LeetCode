package leetcode

func numJewelsInStones(J string, S string) int {
	myDict := make(map[rune]int, len(J))
	for _, v := range J{
		myDict[v] = 1
	}
	res := 0
	for _, v := range S{
		_, ok := myDict[v]
		if ok{
			res ++
		}
	}
	return res
}

// 这有点时间换空间的感觉，感觉和上面的方法差不太多，主要就少了一个map
func numJewelsInStones1(J string, S string) int {
    count := 0
    in := func(slice string, s string) bool {
        for _, el := range slice {
            if string(el) == s {
                return true
            }
        }
        return false
    }
    for _, el := range S {
        if in(J, string(el)){
            count++
        }
    }
    return count
}