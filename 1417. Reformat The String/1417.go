package leetcode

func reformat(s string) string {
	letter := make([]string, 0, len(s)/2)
	dight := make([]string, 0, len(s)/2)

	for _, v := range s{
		if v>='0' && v<='9'{
			dight = append(dight, string(v))
		}else{
			letter = append(letter, string(v))
		}
	}

	tmp := len(letter)-len(dight)
	if tmp > 1 || tmp < -1{
		return ""
	}

	res := ""
	if len(letter)>len(dight){
		for i,v := range dight{
			res += letter[i]
			res += v
		}
		res += letter[len(letter)-1]
	}else if len(letter)<len(dight){
		for i,v := range letter{
			res += dight[i]
			res += v
		}
		res += dight[len(dight)-1]
	}else{
		for i,v := range letter{
			res += dight[i]
			res += v
		}
	}

	return res
}