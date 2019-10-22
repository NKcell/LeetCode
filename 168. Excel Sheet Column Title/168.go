package leetcode

func convertToTitle(n int) string {
    alphabet := [26]string{"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"}
    res := make([]string, 0 ,1)
    for n > 0{
		mod := (n % 26)-1
		if mod == -1{
			mod = 25
		}
		res = append(res, alphabet[mod])
		if n == 26{
			break
		}
		n = n/26
		if mod == 25{
			n --
		}
	}

	s := ""
	for i:=len(res)-1; i>=0; i--{
		s += res[i]
	}
	return s
}