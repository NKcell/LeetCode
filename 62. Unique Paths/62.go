package leetcode

func uniquePaths(m int, n int) int {
	res := make([][]int, n)
	for i := range res{
		res[i] = make([]int, m)
	}
	for i:=0; i<m; i++{
		res[0][i] = 1
	}
	for i:=0; i<n; i++{
		res[i][0] = 1
	}
	for i:=1; i<m; i++{
		for j:=1; j<n; j++{
			res[j][i] = res[j][i-1]+res[j-1][i]
		}
	}
	return res[n-1][m-1]
}