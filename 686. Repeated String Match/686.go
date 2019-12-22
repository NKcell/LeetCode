package leetcode

import(
	"strings"
)

func repeatedStringMatch(A string, B string) int {
	flag := 1
	tmp := A
	for len(A)*flag < len(B){
		flag++
	}
	for i:=1;i<flag;i++{
		A += tmp
	}
	if strings.Contains(A, B){
		return flag
	}
	A += tmp
	if strings.Contains(A, B){
		return flag+1
	}
	return -1
}

func repeatedStringMatch1(A string, B string) int {
	max := len(B)/len(A) + 2
	n := len(B) / len(A)
	for n <= max {
		str := strings.Repeat(A, n)
		if strings.Contains(str, B) {
			return n
		}
		n++
	}

	return -1
}