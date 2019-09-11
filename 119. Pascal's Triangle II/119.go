package main

import (
	"fmt"
)

func getRow(rowIndex int) []int {
	var mylist []int
	mylist = append(mylist,1)
	for i:=0; i<rowIndex; i++{
		mylist = append([]int{0}, mylist[:]...)
		for j:=0; j<len(mylist)-1; j++{
			mylist[j] = mylist[j] + mylist[j+1]
		}
	}
	return mylist
}

func main(){
	fmt.Println(getRow(4))
}

/*
1. 向切片中插入元素      把切片按照要插入的位置分成两部分 用append函数来插入， 这里插入时用...语法糖来
						也可以根据元素长度提前make一个切片，然后用copy向里面添值

‘…’ 其实是go的一种语法糖。 
它的第一个用法主要是用于函数有多个不定参数的情况，可以接受多个不确定数量的参数。 
第二个用法是slice可以被打散进行传递

*/