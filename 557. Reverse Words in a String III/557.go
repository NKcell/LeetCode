package leetcode

import(
	"strings"
)

func reverseWords(s string) string {
	ssep := strings.Split(s, " ")
	for i,v := range ssep{
		tmp := ""
		for j:=len(v)-1; j>-1; j--{
			tmp += string(v[j])
		}
		ssep[i] = tmp 
	}
	return strings.Join(ssep, " ")
}

func reverseWords1(s string) string {
	bs := []byte(s)
	left := 0
	for i, b := range bs {
		if b == ' ' {
			reverse(&bs, left, i-1)
			left = i + 1
		}
	}
	reverse(&bs, left, len(bs)-1)
	return string(bs)
}

func reverse(src *[]byte, from int, to int) {
	for from < to {
		(*src)[from], (*src)[to] = (*src)[to], (*src)[from]
		from++
		to--
	}
}

func reverseWords2(s string) string {
	var start int
	for end := range s {
		if s[end] == ' ' {
			s = s[:start] + reverseStr(s[start:end]) + s[end:]
			end++
			start = end
		}
	}
	s = s[:start] + reverseStr(s[start:])
	return s
}

func reverseStr(s string) string {
	str := []byte(s)
	for i := 0; i < len(str)/2; i++ {
		str[i], str[len(str)-i-1] = str[len(str)-i-1], str[i]
	}
	return string(str)
}