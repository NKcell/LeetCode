package leetcode

import (
	"strings"
)

func uncommonFromSentences(A string, B string) []string {
	A = A + " " + B
	myList := strings.Split(A, " ")
	myDict := make(map[string]int, len(A))
	for _,v := range myList{
		myDict[v] ++
	}

	res := make([]string, 0)
	for i, v := range myDict{
		if v<2{
			res = append(res, i)
		}
	}

	return res
}