package leetcode

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type TreeNode struct {
	Val int
	Left *TreeNode
	Right *TreeNode
}

func pathSum(root *TreeNode, sum int) [][]int {
	res := make([][]int, 0)
	tmp := make([]int, 0)

	dfs(&res, tmp, root, sum)

	return res
}

func dfs(res *[][]int, tmp []int, root *TreeNode, sum int){
	if root == nil{
		return
	}

	sum -= root.Val
	tmp = append(tmp, root.Val)
	if sum==0 && root.Left==nil && root.Right==nil{
		*res = append(*res, tmp)
	}

	tmp1 := make([]int, len(tmp))
	tmp2 := make([]int, len(tmp))
	copy(tmp1, tmp)
	copy(tmp2, tmp)

	dfs(res, tmp1, root.Left, sum)
	dfs(res, tmp2, root.Right, sum)
}