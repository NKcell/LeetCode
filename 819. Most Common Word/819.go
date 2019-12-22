package leetcode

import(
	"strings"
	"sort"
)

func mostCommonWord(paragraph string, banned []string) string {
    resstr := strings.Replace(strings.Replace(strings.Replace(strings.Replace(strings.Replace(strings.Replace(paragraph, ",", " ", -1), ".", " ", -1), "?", " ", -1), ";", " ", -1), "!", " ", -1), "'", " ", -1)
	reslist := strings.Split(resstr, " ")
	for i,v := range reslist{
		reslist[i] = strings.ToLower(v)
	}

	resmap := make(map[string]int, 0)
	for _,v := range reslist{
		resmap[v] ++
	}

	for _, v := range banned{
		delete(resmap, v)
	}

	sortlist := make([]int, 0)
	for _,v := range resmap{
		sortlist = append(sortlist, v)
	}
	sort.Ints(sortlist)
	for i:=len(sortlist)-1;i>=0;i--{
		for value, mapv := range resmap{
			if mapv == sortlist[i]{
				if value == ""{
					continue
				}
				return value
			} 
		}
	}
	return ""
}