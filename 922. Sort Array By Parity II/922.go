package main

import(
	"fmt"
)

func main(){
	fmt.Println(sortArrayByParityII([]int{1,2,3,4}))
}

func sortArrayByParityII(A []int) []int {
	odd := make([]int, 0)
	even := make([]int, 0)
	for _,v := range A{
		if v%2 == 0{
			even = append(even, v)
		}else{
			odd = append(odd, v)
		}
	}
	for i,_ := range A{
		if i%2 == 0{
			A[i] = even[i/2]
		}else{
			A[i] = odd[i/2]
		}
	}
	return A
}