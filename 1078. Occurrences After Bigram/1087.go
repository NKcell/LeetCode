package leetcode

import (
	"strings"
)

func findOcurrences(text string, first string, second string) []string {
	mylist := strings.Split(text, " ")
	res := make([]string, 0)
	for i:=0; i<len(mylist)-2; i++{
		if mylist[i]==first && mylist[i+1]==second{
			res = append(res, mylist[i+2])
		}
	}
	return res
}