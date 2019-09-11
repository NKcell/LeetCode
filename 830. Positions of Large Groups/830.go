package  main

import "fmt"

func main(){
	fmt.Println(largeGroupPositions("abcdddeeeeaabbbcd"))
}

func largeGroupPositions(S string) [][]int {
	var mylist [][]int
	pre := 0
	slen := 0
	for i:=0; i<len(S); i++{
		if S[pre] == S[i]{
			slen ++
		}else{
			if slen>2{
				mylist = append(mylist, []int{pre, i-1})
			}
			slen = 1
			pre = i
		}
	}
	if slen>2{
		mylist = append(mylist, []int{pre, len(S)-1})
	}
	return mylist
}