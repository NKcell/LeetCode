package leetcode

import(
	"strings"
)

func checkRecord(s string) bool {
	a, l := 0, 0
    for _, v := range s{
		if v == 'A'{
			a++
		}
		if v == 'L'{
			l++
		}else{
			l=0
		}

		if a>1 || l>2{
			return false
		}
	}
	return true
}

func checkRecord1(s string) bool {
    return !(strings.Count(s, `A`) > 1) && !strings.Contains(s, `LLL`)
}