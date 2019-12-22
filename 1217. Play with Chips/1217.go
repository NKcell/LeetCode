package leetcode

func minCostToMoveChips(chips []int) int {
	ans := make([]int, 2)
	for _, v := range chips{
		ans[v%2] ++
	}
	if ans[0]<ans[1]{
		return ans[0]
	}
	return ans[1]
}