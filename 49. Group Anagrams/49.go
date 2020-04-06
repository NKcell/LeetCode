package leetcode

import(
	"strings"
	"sort"
)

func groupAnagrams(strs []string) [][]string {
    myDict := make(map[string][]string, 0)
	
	for _, v := range strs{
		tmpSplit := strings.Split(v, "")
		sort.Strings(tmpSplit)
		v1,ok := myDict[strings.Join(tmpSplit,"")]
		if ok{
			v1 = append(v1, v)
			myDict[strings.Join(tmpSplit,"")] = v1
		}else{
			myDict[strings.Join(tmpSplit,"")] = []string{v}
		}
	}

	res := make([][]string, 0)
	for _, v := range myDict{
		res = append(res, v)
	}
	return res
}