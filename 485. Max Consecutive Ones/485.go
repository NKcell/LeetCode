package  main

import "fmt"

func main(){
	fmt.Println(findMaxConsecutiveOnes([]int{1,0,1,1,0,1}))
}

func findMaxConsecutiveOnes(nums []int) int {
	fin := 0
	tmp := 0
    for _, value := range nums{
		if value == 1{
			tmp++
		}else{
			if fin < tmp{
				fin = tmp
			}
			tmp = 0
		}
	}
	if fin < tmp{
		fin = tmp
	}
	return fin
}

func findMaxConsecutiveOnes1(a []int) int {
    best, crt := 0, 0
    for _, v := range a {
        if crt+v > best {
            best = crt+v
        }
        crt = (crt+v)*v
    }
    return best
}