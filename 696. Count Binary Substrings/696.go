package leetcode

import(
	"math"
)

func countBinarySubstrings(s string) int {
	res := make([]int, 0, 1)
	pre := 0
	for i:=1; i<len(s); i++{
		if s[i] != s[i-1]{
			res = append(res, i-pre)
			pre = i
		}
	}
	res = append(res, len(s)-pre)

	pre = 0
	for i:=1; i<len(res);i++{
		if res[i]<res[i-1]{
			pre+=res[i]
		}else{
			pre+=res[i-1]
		}
	}
	return pre
}

func countBinarySubstrings1(s string) int {
	var cur, pre, res float64
    cur = 1  
	for i := 1; i < len(s); i++ {
		if s[i-1] == s[i] {
			cur++
		} else {
			res += math.Min(cur, pre)
			pre = cur
			cur = 1
		}
	}
	return int(res + math.Min(cur, pre))
}