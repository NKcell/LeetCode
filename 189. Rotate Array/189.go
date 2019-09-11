package main

import "fmt"

func main(){
	nums := []int{1,2,3,4,5,6,7}
	rotate(nums, 7)
	fmt.Println(nums)
}

func rotate(nums []int, k int)  {
	k = k%len(nums)
	tmp := append(nums[len(nums)-k:],nums[:len(nums)-k]...)
	for i:=0; i<len(nums); i++{
		nums[i]=tmp[i]
	}
}

func rotate1(nums []int, k int)  {
    nlen := len(nums)
    if k > nlen{
        k = k % nlen
    }
    
    if (k < nlen) && (k != 0){
        
        for i:=0;i< nlen/2;i++{
            nums[i],nums[nlen-i-1] = nums[nlen-i-1],nums[i]
        }
    
        for i:=0;i< k/2;i++{
            nums[i],nums[k-i-1] = nums[k-i-1],nums[i]
        }
    
        for i:=k;i<(nlen + k)/2;i++{
            nums[i], nums[nlen+k-i-1]= nums[nlen+k-i-1],nums[i]
        }
    }
    
}