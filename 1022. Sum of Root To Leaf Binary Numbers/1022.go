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

 func sumRootToLeaf(root *TreeNode) int {
    res := make([]int, 0)
	if root!=nil{
		getValue(root, root.Val, &res)
	}

	count := 0
	for _, v := range res{
		count += v
	}
	return count
}

func getValue(root *TreeNode, value int, res *[]int){
	if root.Left == nil && root.Right == nil{
		*res = append(*res, value)
		return 
	}

	value *= 2
	if root.Left != nil{
		getValue(root.Left, value+root.Left.Val, res)
	}
	if root.Right != nil{
		getValue(root.Right, value+root.Right.Val, res)
	}
}