package leetcode

func firstUniqChar(s string) int {
	myDict := make(map[rune]int, 0)
	for _, v := range s{
		myDict[v]++
	}
	for i, v := range s{
		if myDict[v] == 1{
			return i
		}
	}
	return -1
}

// 这就是利用列表，因为只有26个字母所以不会向上面字典那样动态扩容，效率就会提高很多
func firstUniqChar1(s string) int {
	magic := [26]int{}
	for i := range magic {
		magic[i] = -1
	}
	for i, v := range s {
		if magic[v-'a'] == -1 {
			magic[v-'a'] = i
		} else {
			magic[v-'a'] = -2
		}
	}
	ret := len(s) + 1
	for _, v := range magic {
		if v >= 0 {
			if v < ret {
				ret = v
			}
		}
	}
	if ret == len(s) + 1 {
		ret = -1
	}
	return ret
}

// 和上面方法类似
func firstUniqChar2(s string) int {
    m := [26]int{}
	a := rune('a')
	for _, c := range s {
        m[c-a] += 1
	}
    for i,c := range s{
        if m[c-a] == 1{
            return i
        }
    }
    return -1
}