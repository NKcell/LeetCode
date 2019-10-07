package leetcode

func longestPalindrome(s string) int {
	flag, res := 0, 0
	myDict := make(map[rune]int, 0)
	for _, v := range s{
		myDict[v]++
	}
	for i := range myDict{
		if myDict[i]%2 == 0{
			res+=myDict[i]
		}else{
			if flag == 0{
				flag = 1
			}
			res += (myDict[i]-1)
		}
	}
	return (res+flag)
}