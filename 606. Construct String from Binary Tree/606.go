package leetcode

import(
	"strings"
	"strconv"
)

type TreeNode struct {
	Val int
	Left *TreeNode
	Right *TreeNode
}

func tree2str(t *TreeNode) string {
	res := make([]string, 0)
	if t == nil{
		return ""
	}
	res = append(res, strconv.Itoa(t.Val))
	if t.Left != nil || t.Right != nil{
		tree(t.Left, &res)
		if t.Right != nil{
			tree(t.Right, &res)
		}
	}
	return strings.Join(res, "")
}

func tree(t *TreeNode, res *[]string){
	if t == nil{
		*res = append(*res, "()")
	}else{
		*res = append(*res, "(")
		*res = append(*res, strconv.Itoa(t.Val))
		if t.Left != nil || t.Right != nil{
			tree(t.Left, res)
			if t.Right != nil{
				tree(t.Right, res)
			}
		}
		*res = append(*res, ")")
	}
}

func tree2str1(t *TreeNode) string {
    
    if t == nil { return "" }
    s := strconv.Itoa(t.Val)
    l := tree2str(t.Left)
    r := tree2str(t.Right)
    
    if t.Left == nil && t.Right == nil {
        return s
    }
    if t.Right == nil {
        return s + "(" + l + ")"
    }
    
    return s + "(" + l + ")" + "(" + r + ")"
    
}

func tree2str2(t *TreeNode) string {
	if t == nil {
		return ""
	}
	if t.Left == nil && t.Right == nil {
		return strconv.Itoa(t.Val)
	}
	if t.Left != nil && t.Right == nil {
		return strconv.Itoa(t.Val) + "(" + tree2str(t.Left) + ")"
	}

	if t.Left == nil && t.Right != nil {
		return strconv.Itoa(t.Val) + "()" + "(" + tree2str(t.Right) + ")"
	}

	return strconv.Itoa(t.Val) + "(" + tree2str(t.Left) + ")(" + tree2str(t.Right) + ")"
}