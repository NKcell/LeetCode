package leetcode

func canConstruct(ransomNote string, magazine string) bool {
	myDict1 := make(map[rune]int, 0)
	myDict2 := make(map[rune]int, 0)
	for _,v := range ransomNote{
		myDict1[v]++
	}
	for _,v := range magazine{
		myDict2[v]++
	}

	for i,v := range myDict1{
		if v>myDict2[i]{
			return false
		}
	}
	return true
}

func canConstruct2(ransomNote string, magazine string) bool {
	tmp := make([]int, 26)
	for _, v := range magazine {
		tmp[v-'a']++
	}
	for _, v := range ransomNote {
		tmp[v-'a']--
		if tmp[v-'a'] < 0 {
			return false
		}
	}
	return true
}