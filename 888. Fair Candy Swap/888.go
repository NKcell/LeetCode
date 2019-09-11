package main

import "fmt"

func main(){
	fmt.Println(fairCandySwap([]int{1,2,5}, []int{2,4}))
}

func fairCandySwap(A []int, B []int) []int {
	sumA := sum(A)
	sumB := sum(B)
	dif := sumA - (sumA+sumB)/2
	mymap := make(map[int]int)
	for _,v := range A{
		_,ok := mymap[v-dif]
		if !ok{
			mymap[v-dif] = v
		}
	}
	for _, v := range B{
		a, ok := mymap[v]
		if ok{
			return []int{a, v}
		}
	}
	return []int{}
}

func sum(ele []int)int{
	var s int
	for _,v := range ele{
		s += v
	}
	return s
}