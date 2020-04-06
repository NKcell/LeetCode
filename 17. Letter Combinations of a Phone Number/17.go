package leetcode

import(
	"strings"
)

func letterCombinations(digits string) []string {
	if len(digits) == 0{
		return []string{}
	}

	myMap := make(map[string][]string)
	myMap["2"] = []string{"a", "b", "c"}
	myMap["3"] = []string{"d", "e", "f"}
	myMap["4"] = []string{"g", "h", "i"}
	myMap["5"] = []string{"j", "k", "l"}
	myMap["6"] = []string{"m", "n", "o"}
	myMap["7"] = []string{"p", "q", "r", "s"}
	myMap["8"] = []string{"t", "u", "v"}
	myMap["9"] = []string{"w", "x", "y", "z"}

	res := []string{""}
	newdigits := strings.Split(digits, "")
	
	return dfs(myMap, res, 0, newdigits)
}

func dfs(myMap map[string][]string, res []string, index int, digits []string) []string{
	if len(digits) <= index{
		return res
	}

	newres := make([]string, 0, len(res)*len(myMap[digits[index]]))
	for _, v1 := range res{
		for _, v2 := range myMap[digits[index]]{
			newres = append(newres, v1+v2)
		}
	}

	return dfs(myMap, newres, index+1, digits)
}