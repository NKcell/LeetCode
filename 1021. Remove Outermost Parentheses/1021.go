package leetcode

import(
	"strings"
)

func removeOuterParentheses(S string) string {
	pre := 0
	res := make([]string, 0)
	flag := 0
	for i,v := range S{
		if v == '('{
			flag ++
		}else{
			flag --
		}

		if flag == 0{
			res = append(res, S[pre+1: i])
			pre = i+1
		}
	}

	return strings.Join(res, "")
}

func removeOuterParentheses1(S string) string {
	var sb strings.Builder
	i, count, size := 0, 0, len(S)
	for j := 0; j < size; j++ {
		if S[j] == '(' {
			count++
		} else {
			count--
		}
		if count == 0 {
			sb.WriteString(S[i+1 : j])
			i = j + 1
		}
	}
	return sb.String()
}