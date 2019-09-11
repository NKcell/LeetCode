package main

import "fmt"

func main(){
	fmt.Println(canPlaceFlowers([]int{1,0,0,0,1}, 2))
}

func canPlaceFlowers(flowerbed []int, n int) bool {
	flowerbed = append(flowerbed,0)
	flowerbed = append([]int{0}, flowerbed[:]...)
	count := 0
	for _,value := range flowerbed{
		if value == 1{
			count = 0
		}else{
			count ++
		}

		if count == 3{
			n--
			count = 1
		}

		if n == 0{
			return true
		}
	}
	return false
}