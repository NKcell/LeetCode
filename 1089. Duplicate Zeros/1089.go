package  leetcode

func duplicateZeros(arr []int)  {
	tmp := make([]int,0,len(arr))
	for i,v := range arr{
		if len(tmp)!=len(arr){
			if v == 0{
				tmp = append(tmp, 0,0)
			}else{
				tmp = append(tmp, v)
			}
		}

		arr[i] = tmp[i]
	}
}

// 不进行内存分配是要快很多啊
func duplicateZeros1(A []int) {
	n := len(A)
	//
	count := 0
	for i := 0; i < n; i++ {
		if A[i] == 0 {
			count++
		}
	}
	// copy A[i] to A[j]
	copy := func(i, j int) {
		if j < n {
			A[j] = A[i]
		}
	}
	//
	i, j := n-1, n+count-1
	for i < j {
		if A[i] == 0 {
			copy(i, j)
			j--
			copy(i, j)
		} else {
			copy(i, j)
		}
		i--
		j--
	}
}