package leetcode

import (
	"strings"
	"strconv"
)

func subdomainVisits(cpdomains []string) []string {
	myDict := make(map[string]int, 1)
	for _, v := range cpdomains{
		tmp := strings.Split(v, " ")
		value, _ := strconv.Atoi(tmp[0])
		domain := strings.Split(tmp[1], ".")

		tmpstr := ""
		for i:=len(domain)-1; i>-1; i--{
			v2 := domain[i]
			tmpstr = v2 + tmpstr
			myDict[tmpstr] += value
			tmpstr = "." + tmpstr
		}
	}
	
	res := make([]string, 0 ,len(myDict))
	for i, v := range myDict{
		res = append(res, strconv.Itoa(v)+" "+i)
	}
	return res
}

// 这个自己实现split要快很多 测试显示动态开辟内存次数会变少？？？
func subdomainVisits1(cpdomains []string) []string {
	tempSlice := []string{}
	tempMap := make(map[string]int)
	var n int
	var s string
	for _, v := range cpdomains {
		for I, V := range v {
			if V == ' ' {
				n, _ = strconv.Atoi(v[:I])
				s = v[I+1:]
			}
		}
		tempMap[s] += n
		for i, v := range s {
			var tempS string
			if v == '.' {
				tempS = s[i+1:]
				tempMap[tempS] += n
			}
		}
	}
	for i, v := range tempMap {
		a := strconv.Itoa(v) + " " + i
		tempSlice = append(tempSlice, a)
	}
	return tempSlice
}