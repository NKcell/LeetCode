package main

import "fmt"

func main(){
	fmt.Println(isOneBitCharacter([]int{0,1,1,1,0}))
}

func isOneBitCharacter(bits []int) bool {
	bits_length := len(bits)
	index := 0
	for index < bits_length{
		if index == bits_length-1{
			return true
		}
		if bits[index] == 1{
			index += 2
		}else{
			index++
		}
	}
	return false
}