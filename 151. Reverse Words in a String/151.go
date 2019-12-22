package leetcode

import(
	"strings"
)

func reverseWords(s string) string {
	res := strings.Split(s, " ")
	res1 := make([]string, 0)
	for i:=len(res)-1; i>=0; i--{
		if res[i] == "" || res[i] == " "{
			continue
		}
		res1 = append(res1, res[i])
	}
	return strings.Join(res1, " ")
}

func reverse(m *[]string, i int, j int){
	for {
        if i > j {
			break
		}
		(*m)[i], (*m)[j] = (*m)[j], (*m)[i]
		i++
		j--
	}
}

func reverseWords1(s string) string {
	ss:=strings.Fields(s)
	reverse(&ss,0,len(ss)-1)
    return strings.Join(ss," ")
}