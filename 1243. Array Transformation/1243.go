package leetcode

func transformArray(arr []int) []int {
	myLen := len(arr)-1
    for {
		tmpList := make([]int,len(arr))
		for i:=1; i<myLen; i++{
			if arr[i]>arr[i+1] && arr[i]>arr[i-1]{
				tmpList[i] = -1
			}else if arr[i]<arr[i+1] && arr[i]<arr[i-1]{
				tmpList[i] = 1
			}
		}

		flag := 0
		for i:=1; i<myLen; i++{
			if tmpList[i] != 0{
				flag++
			}
			arr[i] = arr[i] + tmpList[i]
		}
		if flag == 0{
			return arr
		}
	}
}