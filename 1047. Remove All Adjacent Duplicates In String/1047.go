package leetcode

func removeDuplicates(S string) string {
    res := make([]string, 0)
	for _,v := range S{
		if len(res)!=0{
			if res[len(res)-1] == string(v){
				res = res[0:len(res)-1]
			}else{
				res = append(res, string(v))
			}
		}else{
			res = append(res, string(v))
		}
	}
	return strings.Join(res, "")
}