package main

import(
	"fmt"
)

func main(){
	fmt.Println(numPairsDivisibleBy60([]int{60, 60, 60}))
}

func numPairsDivisibleBy60(time []int) int {
	myMap := make(map[int]int)
	for _,v := range time{
		mapv, ok := myMap[v%60]
		if !ok{
			myMap[v%60]=1
		}else{
			myMap[v%60]=mapv+1
		}
	}

	var count int

	v, ok := myMap[0]
	if ok{
		count += v*(v-1)/2
	}
	v, ok = myMap[30]
	if ok{
		count += v*(v-1)/2
	}

	for i:=1; i<30; i++{
		v1, ok1 := myMap[i]
		v2, ok2 := myMap[60-i]
		if ok1 && ok2{
			count += v1*v2
		}
	}

	return count
}

// 很厉害，好想法
func numPairsDivisibleBy601(time []int) int {
    var (
        count int
        record = make([]int, 60)
    )
    for i := 0; i < len(time); i++ {
        mod := time[i] % 60
        if mod == 0 {
            count += record[0] 
        } else {
            count += record[60-mod]
        }        
        record[mod]++
    }
    return count
}