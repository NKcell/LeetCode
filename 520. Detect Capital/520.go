package leetcode

import (
	"strings"
	"fmt"
)

func detectCapitalUse(word string) bool {
	s1 := strings.ToLower(word)
	s2 := strings.ToUpper(word)
	s3 := word

	
	tmp := []rune(s3)
	for i:=1; i<len(tmp); i++{
		if tmp[i]>='A' && tmp[i]<='Z'{
			tmp[i] += 32
		}
	} 
	s3 = string(tmp)
	
	fmt.Println(s1,s2,s3)
	if s1 == word || s2 == word || s3 == word{
		return true
	}
	return false
}

func detectCapitalUse1(word string) bool {
    return strings.ToLower(word) == word || strings.ToUpper(word) == word || strings.ToLower(word[1:]) == word[1:]
}