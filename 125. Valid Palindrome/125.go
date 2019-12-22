package leetcode

import(
	"unicode"
	"strings"
)

func isPalindrome(s string) bool {
	l, r := 0, len(s)-1
	s = strings.ToUpper(s)

	for l<r{
		if !unicode.IsDigit(rune(s[l])) && !unicode.IsLetter(rune(s[l])){
			l++
			continue
		}
		if !unicode.IsDigit(rune(s[r])) && !unicode.IsLetter(rune(s[r])){
			r--
			continue
		}
		if s[l] != s[r]{
			return false
		}
		l++
		r--
	}

	return true
}