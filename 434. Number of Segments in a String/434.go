package leetcode

func countSegments(s string) int {
	flag := false
	count := 0
	for _, v := range s{
		if v!=' ' && !flag{
			count++
			flag = true
		}
		if v==' '{
			flag = false
		}
	}
	return count
}