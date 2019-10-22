package  leetcode

import(
	"strings"
)

func shortestCompletingWord(licensePlate string, words []string) string {
	licenseDict := make(map[rune]int, 0)
	for _,v := range licensePlate{
		if 0<=v-'a' && v-'a'<=25{
			licenseDict[v-'a']++
		}
		if 0<=v-'A' && v-'A'<=25{
			licenseDict[v-'A']++
		}
	}

	res := "aaaaaaaaaaaaaaaa"
	for _,v := range words{
		tmp := make(map[rune]int, 0)
		for _,v1 := range v{
			if 0<=v1-'a' && v1-'a'<=25{
				tmp[v1-'a']++
			}
		}

		flag := 0
		for i, v2 := range licenseDict{
			if v2>tmp[i]{
				flag = 1
				break
			}
		}
		if flag == 0{
			if len(v)<len(res){
				res = v
			}
		}
	}

	if len(res) < 16{
		return res
	}
	return ""
}

func shortestCompletingWord1(licensePlate string, words []string) string {

    s := ""
	minLen := 16
	index := make([]int, 26, 26)
	tmp := strings.ToLower(licensePlate)
    
	for _, v := range tmp {
		if v >= 'a' && v <= 'z' {
			index[v-'a']++
		}
	}
	for _, v := range words {
		if len(v) >= minLen {
			continue
		}
		if !matches(index, v) {
			continue
		}
		minLen = len(v)
		s = v
	}

	return s

}

func matches(index []int, s string) bool {
	temp := make([]int, 26, 26)
	for _, v := range s {
		temp[v-'a']++
	}
	for i := 0; i < 26; i++ {
		if index[i] > temp[i] {
			return false
		}
	}
	return true
}