package leetcode

func validPalindrome(s string) bool {
	start := 0
	end := len(s)-1

	for start<end{
		if s[start] == s[end]{
			start++
			end--
		}else{
			return lala(s, start+1, end) || lala(s, start, end-1)
		}
	}
	return true
}

func lala(s string, start, end int) bool {
	for start<end{
		if s[start] != s[end]{
			return false
		}
		start++
		end--
	}
	return true
}