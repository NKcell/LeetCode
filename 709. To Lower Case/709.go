package leetcode

import(
	"bytes"
	"unicode"
)

func toLowerCase(str string) string {
	res := ""
    for _,v := range str{
		if v>='A' && v<='Z'{
			res += string((v+32))
		}else{
			res += string(v)
		}
	}
	return res
}

func toLowerCase1(str string) string {
	var lower bytes.Buffer
	for _, e := range str {
		lower.WriteRune(unicode.ToLower(e))
	}
	return lower.String()
}