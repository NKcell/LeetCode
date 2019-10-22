package leetcode

import (
	"math"
	"sort"
)

func longestWord(words []string) string {
	myLen := 1
	myDict := make(map[string]int, 0)
	nextList := make([]string, 0)

	for _,v := range words{
		if len(v) == myLen{
			myDict[v] = 1
		}else{
			nextList = append(nextList, v)
		}
	}
	myLen ++
	words = nextList

	for len(nextList) != 0{
		nextList := make([]string, 0)
		tmp := make(map[string]int, 0)
		for _,v := range words{
			if len(v) == myLen{
				_, ok := myDict[v[:myLen-1]]
				if ok{
					tmp[v] = 1
				}
			}else{
				nextList = append(nextList, v)
			}
		}
		if len(tmp) == 0{
			break
		}
		myLen ++
		words = nextList
		myDict = tmp
	}

	res := "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
	for i := range myDict{
		if res > i{
			res = i
		}
	}
	return res
}

func longestWord1(words []string) string {
    if len(words) < 2 { return "" }
	tmp := []string{}
	max := math.MinInt32
	sort.Slice(words, func(i, j int) bool {
		return len(words[i]) < len(words[j])
	})
	for i := len(words) - 1; i > 0; i-- {
		count := 1
		l := len(words[i])
		for j := i - 1; j >= 0; j-- {
			if words[i][:l-count] == words[j] {
				count++
			}
			if count == l {
				if len(words[i]) > max {
					max = len(words[i])
				}
				if len(words[i]) == max {
					tmp = append(tmp, words[i])
				}
			}
		}
	}
    if len(tmp) == 1 { return tmp[0] }
	res := tmp[0]
	for _, v := range tmp {
		if v < res {
			res = v
		}
	}
	return res
}
