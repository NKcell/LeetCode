package leetcode

func partition(s string) [][]string {
    res := make([][]string, 0)
	tmp := make([]string, 0)

	dfs(&res, tmp, s)

	return res
}

func dfs(res *[][]string, tmp []string, s string){
	if len(s) == 0{
		*res = append(*res, tmp)
		return
	}

	for i := range s{
		if ispar(s[:i+1]){
			newtmp := make([]string, 0, len(tmp)+1)
			newtmp = append(newtmp, tmp...)
			newtmp = append(newtmp, s[:i+1])
			dfs(res, newtmp, s[i+1:])
		}
	}
}

func ispar(s string)bool{
	l := 0
	r := len(s)-1
	for l<r{
		if s[l] != s[r]{
			return false
		}
		l++
		r--
	}
	return true
}