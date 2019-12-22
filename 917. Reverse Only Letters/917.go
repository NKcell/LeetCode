package leetcode

import (
	"unicode"
	"strings"
)

func reverseOnlyLetters(S string) string {
	res := make([]string, len(S))
	pre := 0
	lst := len(S)-1

	for pre<=lst{
		flag := 0
		if !unicode.IsLetter(rune(S[pre])){
			res[pre] = string(S[pre])
			pre++
			flag = 1
		}
		if !unicode.IsLetter(rune(S[lst])){
			res[lst] = string(S[lst])
			lst--
			flag = 1
		}

		if flag == 1{
			continue
		}

		res[pre], res[lst] = string(S[lst]), string(S[pre])
		pre ++
		lst --
	}
	return strings.Join(res, "")
}

func reverseOnlyLetters1(S string) string {
    start, end := 0, len(S) - 1
    ans := []byte(S)
    for start < end {
        for !isLetter(S[start]) && start < end{
            start++
        }
        for !isLetter(S[end]) && start < end {
            end--
        }
        ans[start], ans[end] = ans[end], ans[start]
        start++
        end--
    }
    return string(ans)
}

func isLetter(c byte) bool {
    return c >= 'a' && c <= 'z' || c >= 'A' && c <= 'Z'
}