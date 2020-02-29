/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
package leetcode

type TreeNode struct {
	Val int
	Left *TreeNode
	Right *TreeNode
}

func searchBST(root *TreeNode, val int) *TreeNode {
    return getNode(root, val)
}

func getNode(root *TreeNode, val int) *TreeNode{
	if root == nil{
		return nil
	}else if root.Val == val{
		return root
	}else if root.Val>val{
		return getNode(root.Left, val)
	}else{
		return getNode(root.Right, val)
	}
}