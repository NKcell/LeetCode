package leetcode

import(
	"strings"
)

func repeatedSubstringPattern(s string) bool {
    for i:=len(s)/2; i>0; i--{
		if len(s)%i == 0{
			start := s[:i]
			tmp := ""
			for j:=0; j<len(s)/i; j++{
				tmp += start
			
				if tmp == s{
					return true
				}
			}
		}
	}
	return false
}

func repeatedSubstringPattern1(s string) bool {
	if len(s) == 0 {
		return false
	}
	ss := (s + s)[1 : len(s)*2-1]
	return strings.Contains(ss, s)
}