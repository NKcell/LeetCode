package leetcode

func findSpecialInteger(arr []int) int {
	count := 1
	flag := len(arr)/4

	for i:=1; i<len(arr); i++{
		if count > flag{
			return arr[i-1]
		}
		if arr[i] == arr[i-1]{
			count ++
		}else{
			count = 1
		}
	}
	return arr[len(arr)-1]
}