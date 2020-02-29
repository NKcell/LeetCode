package leetcode

func minAddToMakeValid(S string) int {
    res := make([]rune, 0)
	for _, v := range S{
		if v == '('{
			res = append(res, '(')
		}else{
			if len(res) == 0{
				res = append(res, ')')
			}else if res[len(res)-1] == '('{
				res = res[0:len(res)-1]
			}else{
				res = append(res, ')')
			}
		}
	}
	return len(res)
}