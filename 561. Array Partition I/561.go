package  main

import (
	"fmt";
	"sort"
)

func main(){
	fmt.Println(arrayPairSum([]int{7,3,1,0,0,6}))
}

func arrayPairSum(nums []int) int {
	sort.Ints(nums[:])
	var sum int
	for index,value := range nums{
		if index % 2 == 0{
			sum += value
		}
	}
	return sum
}

func arrayPairSum1(nums []int) int {
    var buckets [20001]int
    for _, v := range nums {
        buckets[v+10000]++
    }
    sum := 0
    odd := true
    for i := 0; i < len(buckets); i++ {
        for buckets[i] > 0 {
            if odd {
                sum += i - 10000
            }
            odd = !odd
            buckets[i]--
        }
    }
    return sum
}