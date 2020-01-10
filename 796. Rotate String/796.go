package leetcode

import(
	"strings"
)

func rotateString(A string, B string) bool {
	tmp := strings.Join([]string{A, A}, "")
	if len(A) == len(B) && strings.Contains(tmp, B){
		return true
	} 
	return false
}

