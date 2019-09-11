package  main

import "fmt"

func main(){
	fmt.Println(findDisappearedNumbers([]int{1,1}))
}

func findDisappearedNumbers(nums []int) []int {
    for _,value := range nums{
		if value < 0 {
			value = -value
		}
		index := value-1
		if nums[index]<0{
			nums[index] = -nums[index]
		}
		nums[index] = -nums[index] 
	}

	renums := make([]int, 0)

	for index, value := range nums{
		if value > 0{
			renums = append(renums, index+1)
		}
	}
	return renums
}

func findDisappearedNumbers1(nums []int) []int { 
    for i := 0; i < len(nums); i++ {
        if i + 1 == nums[i] || nums[i] == 0 {
            continue
        }
        
        // correct value already in swap place
        if nums[i] == nums[nums[i] - 1] {
            nums[i] = 0
            continue
        }
        
        // swap
        nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]
        
        // redo this spot
        i--
    }
    
    // convert existing numbers to zeros and add missing numbers
    for i := 0; i < len(nums); i++ {
        if (nums[i] == 0) {
            nums[i] = i + 1
            continue
        }
        
        nums[i] = 0 
    }
    
    // delete zeros
    for i := 0; i < len(nums); i++ {
        if (nums[i] == 0) {   
            nums = append(nums[:i], nums[i+1:]...) 
            i--
        }
    }
    
    return nums
}