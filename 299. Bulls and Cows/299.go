package leetcode

import(
	"strconv"
)

func getHint(secret string, guess string) string {
	mydict := make(map[rune]int)
	cows := 0
	bull := 0

	for _, v := range secret{
		dictv, ok := mydict[v]
		if ok{
			mydict[v] = dictv + 1
		}else{
			mydict[v] = 1
		}
	}

	for i, v := range guess{
		dictv, ok := mydict[v]
		if ok && dictv>0{
			cows++
			mydict[v] = dictv-1
		}
		if v == rune(secret[i]){
			cows--
			bull++
		}
	}
	return strconv.Itoa(bull)+"A"+strconv.Itoa(cows)+"B"
}