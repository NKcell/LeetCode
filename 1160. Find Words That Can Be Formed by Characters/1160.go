package leetcode

func countCharacters(words []string, chars string) int {
	var count int
	mymap := make(map[rune]int, len(chars))
	for _, v := range chars{
		mapv, ok := mymap[v]
		if !ok{
			mymap[v] = 1
		}else{
			mymap[v] = mapv + 1
		}
	}

	for _, v := range words{
		tmpmap := make(map[rune]int, len(v))
		for _, v1 := range v{
			mapv, ok := tmpmap[v1]
			if !ok{
			tmpmap[v1] = 1
			}else{
				tmpmap[v1] = mapv + 1
			}
		}

		var flag int
		for i, v2 := range tmpmap{
			if v2 > mymap[i]{
				flag = 1
				break
			}
		}
		if flag == 0{
			count += len(v)
		}
	}

	return count
}


// 前面也是想用切片来做啊，但不知道byte和int的转换
// 但这里发现用rune相减是int可以作为下标去索引...
func countCharacters1(words []string, chars string) int {
	char := parse(chars)
	res := 0
	for _, word := range words {
		res += count(char, word)
	}
	return res
}

func parse(s string) []int {
	res := make([]int, 26)
	for _, r := range s {
		res[r-'a']++
	}
	return res
}

func count(char []int, word string) int {
	res := 0
	w := make([]int, 26)
	for _, r := range word {
		b := r - 'a'
		w[b]++
		if w[b] > char[b] {
			return 0
		}
		res++
	}
	return res
}