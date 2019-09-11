package leetcode

import "sort"

func numSmallerByFrequency(queries []string, words []string) []int {
	queriesNum := make([]int, len(queries))
	wordsNum := make([]int, len(words))
	for i:=0; i<len(queries); i++{
		queriesNum[i] = countFrequency(queries[i])
	}
	for i:=0; i<len(words); i++{
		wordsNum[i] = countFrequency(words[i])
	}
	
	sort.Sort(sort.Reverse(sort.IntSlice(wordsNum)))
	for i, vq := range queriesNum{
		var count int
		for _, vw := range wordsNum{
			if vw>vq{
				count ++
			}else{
				break
			}
		}
		queriesNum[i] = count
	}
	return queriesNum
}

func countFrequency(words string) int{
	myslice := make([]int, 26)
	for _,i := range words{
		myslice[i-'a']++
	}
	for _,i := range myslice{
		if i != 0{
			return i
		}
	}
	return 0
}

// 这个用了search的方法, 效果基本一样
func numSmallerByFrequency1(queries []string, words []string) []int {
    var ans []int
    count := make([]int, len(words))
    for i, w := range words {
        count[i] = countFrequency(w)
    }
    sort.Ints(count)
    for _, q := range queries {
        ans = append(ans, len(count) - sort.SearchInts(count, countFrequency(q)+1))
    }
    return ans
}