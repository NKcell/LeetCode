package leetcode

func replaceElements(arr []int) []int {
	maxnum := -1
	for i:=len(arr)-1; i>-1; i--{
		tmp := arr[i]
		arr[i] = maxnum
		if tmp>maxnum{
			maxnum = tmp
		}
	}
	return arr
}