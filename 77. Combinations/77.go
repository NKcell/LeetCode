package leetcode

func combine(n int, k int) [][]int {
	nums := make([]int, 0, n)
	for i:=1; i<n+1; i++{
		nums = append(nums, i)
	}

	res := make([][]int, 0)

	dfs(k, &res, []int{}, nums)
	return res
}

func dfs(n int, res *[][]int, tmp []int, nums []int){
	if n == 0{
		*res = append(*res, tmp)
	}

	if len(nums)<n{
		return
	}

	for i,v := range nums{
		if len(nums) - i < n{
			break
		}
		newtmp := make([]int, 0, len(tmp)+1)
		newtmp = append(newtmp, tmp...)
		newtmp = append(newtmp, v)

		newnums := make([]int, 0, len(nums)-i-1)
		newnums = append(newnums, nums[i+1:]...)

		dfs(n-1, res, newtmp, newnums)
	}
}