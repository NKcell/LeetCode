package leetcode

func generateParenthesis(n int) []string {
    if n == 0{
		return []string{}
	}

	res := make([]string, 0)

	r := n
	l := 0

	dfs(&res, "", 2*n, r, l)

	return res
}

func dfs(res *[]string, tmpStr string, n, r, l int){
	if len(tmpStr) == n{
		*res = append(*res, tmpStr)
	}

	if r != 0{
		dfs(res, tmpStr+"(", n, r-1, l+1)
	}
	if l != 0{
		dfs(res, tmpStr+")", n, r, l-1)
	}
}