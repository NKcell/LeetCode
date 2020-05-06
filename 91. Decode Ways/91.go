package leetcode

import(
	"strconv"
)

func numDecodings(s string) int {
    if len(s) == 0{
		return 0
	}

	v := 0
	w := 1
	p := "0"
	mys := strings.Split(s, "")

	for _,letter := range mys{
		tmp := 0
		if letter != "0"{
			tmp += w
		}
		ge, _ := strconv.Atoi(letter)
		shi, _ := strconv.Atoi(p)
		value := ge + shi*10
		if value>9 && value<27{
			tmp += v
		}
		v = w
		w = tmp
		p = letter
	}

	return w
}