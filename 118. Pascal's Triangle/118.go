package main

import(
	"fmt"
)

func generate(numRows int) [][]int{
	var mylist [][]int
	var first []int = []int{1}
	var second []int = []int{1, 1}
	
	for i:=0; i<numRows; i++{
		if i == 0{
			mylist = append(mylist, first)
		}else if i == 1{
			mylist = append(mylist, second)
		}else{
			var tmp []int = []int{1}
			for j:=0 ; j<i-1 ; j++{
				tmp = append(tmp, mylist[i-1][j]+mylist[i-1][j+1])
			}
			tmp = append(tmp, 1)
			mylist = append(mylist, tmp)
		}
	}

	return mylist
}

//好方法，思路如python中所述
func generate1(numRows int) [][]int {
	if numRows == 0 {
		return [][]int{}
	}
    if numRows == 1 {
        return [][]int{{1}}
    }
	res := [][]int{{1}}
	for i := 1; i < numRows; i++ {
		var arr []int
		for j := 0; j < i + 1; j++ {
			left, right := 0, 0
			if j - 1 >= 0 {
				left = res[i-1][j-1]
			}
			if j < len(res[i-1]) {
				right = res[i-1][j]
			}
			arr = append(arr, left+right)
		}
		res = append(res, arr)
	}
	return res
}

func main(){
	fmt.Println(generate(5))
}

/*
	首先append，不能append(xxx, [1])   append(xxx, []int{1})       [][]int{{1}}
*/