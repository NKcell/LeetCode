package leetcode

func permute(nums []int) [][]int {
    res := make([][]int, 0)
	tmp := []int{}

	dfs(&res, nums, tmp)

	return res
}

func dfs(res *[][]int, nums []int, tmp []int){
	if len(nums) == 0{
		*res = append(*res, tmp)
        return
	}

	for i:=0; i<len(nums); i++{
		newtmp := make([]int, 0, len(tmp)+1) 
		newtmp = append(newtmp, tmp...)
		newtmp = append(newtmp, nums[i])
		newnums := make([]int, 0,len(nums)-1)
		newnums = append(newnums, nums[:i]...)
		newnums = append(newnums, nums[i+1:]...)
		dfs(res, newnums, newtmp)
	}
}