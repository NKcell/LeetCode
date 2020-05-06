package leetcode

func destCity(paths [][]string) string {
	res := make(map[string]int, 2)
	
	for _,v := range paths{
		if _,ok := res[v[0]]; ok{
			delete(res, v[0])
		}else{
			res[v[0]] = 0
		}

		if _,ok := res[v[1]]; ok{
			delete(res, v[1])
		}else{
			res[v[1]] = 1
		}
	}

	for i,v := range res{
		if v == 1{
			return i
		}
	}

	return ""
}