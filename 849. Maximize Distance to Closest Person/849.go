package main

import(
	"fmt";
	"math"
)

func main(){
	fmt.Println(maxDistToClosest([]int{1,0,0,1}))
}

func maxDistToClosest(seats []int) int {
	flag := -1
	start := -1
	var maxlength int
    for index, value := range seats{
		if value == 1 && flag == -1{
			flag = index
		}
		if value == 1{
			maxlength = int(math.Max(math.Ceil(float64(index-start-1)/float64(2)), float64(maxlength)))
			start = index
		}
	}
	return int(math.Max(float64(maxlength), math.Max(float64(flag), float64(len(seats)-start-1))))
}