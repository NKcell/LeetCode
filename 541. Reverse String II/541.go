package leetcode

import (
	"strings"
)

func reverseStr(s string, k int) string {
	mySep := strings.Split(s, "")
	count := 0
	for count*k < len(s) {
		if (count+1)*k < len(s) {
			myReverse(mySep, count*k, (count+1)*k)
		} else {
			myReverse(mySep, count*k, len(s))
		}
		count += 2
	}
	return strings.Join(mySep, "")
}

func myReverse(mySep []string, start, end int) {
	for i := 0; i < (end-start)/2; i++ {
		mySep[start+i], mySep[end-i-1] = mySep[end-i-1], mySep[start+i]
	}
}

// string直接与[]byte转快很多
func reverseStr1(s string, k int) string {
	tmp := []byte(s)
	end := len(tmp) - 1
	for i := 0; i <= end; i += 2 * k {
		x := i
		y := i + k - 1
		if y > end {
			y = end
		}
		for x < y {
			tmp[x], tmp[y] = tmp[y], tmp[x]
			x++
			y--
		}
	}
	return string(tmp)
}
