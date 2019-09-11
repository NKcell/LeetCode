package  main

import "fmt"

func main(){
	fmt.Println(matrixReshape([][]int{{1,2},{3,4}},2,4))
}

func matrixReshape(nums [][]int, r int, c int) [][]int {
    if len(nums)*len(nums[0]) != r*c{
		newnums := make([][]int, len(nums))
		for i := 0; i < len(nums); i++ {
			newnums[i] = make([]int, len(nums[0]))
			copy(newnums[i], nums[i])
		}
		return newnums
	}

	onenums := make([]int, r*c)
	count := 0
	for _,i := range nums{
		for _,value := range i{
			onenums[count] = value
			count++
		}
	}


	newnums := make([][]int, r)
	for i := 0; i < r; i++ {
		newnums[i] = make([]int, c)
		copy(newnums[i], onenums[c*i:c*(i+1)])
	}
	return newnums

}

/*
这里还是强调一下二维数组的初始化、
ans := make([][]int, r)
    for i:=0; i<r; i++ {
        ans[i] = make([]int, c)
    }
*/