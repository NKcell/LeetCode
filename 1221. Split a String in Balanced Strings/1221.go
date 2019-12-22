package leetcode

func balancedStringSplit(s string) int {
	l, r, res := 0, 0, 0
	for _,v := range s{
		if v == 'L'{
			l++
		}else{
			r++
		}

		if l==r{
			res++
		}
	}
	return res
}