package leetcode

func dailyTemperatures(T []int) []int {
	res := make([]int, len(T))
	mydict := make(map[int]int, 0)

	for i:=len(T)-1; i>-1; i--{
		tmp := 30001
		for j:=T[i]+1; j<101; j++{
			if v, ok := mydict[j]; ok{
				if v-i<tmp{
					tmp = v-i
				}
			} 
		}
		if tmp != 30001{
			res[i] = tmp
		}
		mydict[T[i]] = i;
	} 
	return res
}