package leetcode

import(
	"strings"
)

func reverseVowels(s string) string {
	myvowels := make([]rune, 0)
	for _,v := range s{
		if v == 'a' || v == 'e' || v == 'i' || v == 'o' || v == 'u' || v == 'A' || v == 'E' || v == 'I' || v == 'O' || v == 'U'{
			myvowels = append(myvowels,v)
		}
	}
	res := ""
	flag := len(myvowels)-1
	for _,v := range s{
		if v != 'a' && v != 'e' && v != 'i' && v != 'o' && v != 'u' && v != 'A' && v != 'E' && v != 'I' && v != 'O' && v != 'U'{
			res += string(v)
		}else{
			res += string(myvowels[flag])
			flag --
		}
	}
	return res
}

func reverseVowels1(s string) string {

	sByte := []byte(s)
	i, j := 0, len(s)-1
	for i < j {
		for i < j && !isVowel(sByte[i]) {
			i++
		}
		for i < j && !isVowel(sByte[j]) {
			j--
		}

		sByte[i], sByte[j] = sByte[j], sByte[i]
		i++
		j--

	}
	return string(sByte)
}

func isVowel(b byte) bool {
	if b == byte('a') || b == byte('e') || b == byte('i') || b == byte('o') || b == byte('u') ||
		b == byte('A') || b == byte('E') || b == byte('I') || b == byte('O') || b == byte('U') {
		return true
	}
	return false
}

func reverseVowels2(s string) string {
	vowels := "aeiouAEIOU"
	start := 0
	end := len(s) - 1
	st := []rune(s)

	for start < end {
		if strings.ContainsRune(vowels, st[start]) && strings.ContainsRune(vowels, st[end]){
			tmp := st[start]
			st[start] = st[end]
			st[end] = tmp
			start++
			end--
		} else if strings.ContainsRune(vowels, st[start]) {
			end--
		} else if strings.ContainsRune(vowels, st[end]) {
			start++
		} else {
			start++
			end--
		}
	}

	return string(st)
}