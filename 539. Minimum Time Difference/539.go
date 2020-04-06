package leetcode

import(
	"strings"
	"strconv"
	"sort"
)

func findMinDifference(timePoints []string) int {
	timeList := make([]int, 0, len(timePoints))
	for _,v := range timePoints{
		hm := strings.Split(v, ":")
		hour,_ := strconv.Atoi(hm[0])
		minute,_ := strconv.Atoi(hm[1])
		timeList = append(timeList, hour*60+minute)
	}

	sort.Ints(timeList)

	minvalue := timeList[1]-timeList[0]

	for i:=2;i<len(timeList);i++{
		tmp := timeList[i]-timeList[i-1]
		if tmp<minvalue{
			minvalue = tmp
		}
	}

	tmp:=60*24+timeList[0]-timeList[len(timeList)-1]
	if tmp<minvalue{
		return tmp
	}
	return minvalue
}