package leetcode

import (
	"strconv"
	"strings"
)

func rotatedDigits(N int) int {
	count := 0
	for i := 0; i <= N; i++ {
		is := strconv.Itoa(i)
		if strings.ContainsRune(is, '3') || strings.ContainsRune(is, '4') || strings.ContainsRune(is, '7') {
			continue
		}
		if strings.ContainsRune(is, '2') || strings.ContainsRune(is, '5') || strings.ContainsRune(is, '6') || strings.ContainsRune(is, '9') {
			count++
		}
	}
	return count
}

func rotatedDigits1(N int) int {
	nums := []rune{'0', '1', '5', '-', '-', '2', '9', '-', '8', '6'}
	count := 0
	for i := 1; i <= N; i++ {
		s := strconv.Itoa(i)
		same := 0
		for i, v := range s {
			if nums[v-'0'] == '-' {
				break
			}
			if nums[v-'0'] == v {
				same++
			}
			if same != len(s) && i == len(s)-1 {
				count++
			}
		}
	}
	return count
}
