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

type FindElements struct {
    root *TreeNode
}


func Constructor(root *TreeNode) FindElements {
    if root != nil{
		root.Val = 0
	}
	recover(root)
	var newroot  = FindElements{root}
	return newroot
}

func recover(root *TreeNode){
	if root.Left != nil{
		root.Left.Val = root.Val*2+1
		recover(root.Left)
	}
	if root.Right != nil{
		root.Right.Val = root.Val*2+2
		recover(root.Right)
	}
}


func (this *FindElements) Find(target int) bool {
	res := make([]int,0)
	res = append(res, target)
	for target != 0{
		if target%2 == 0{
			target = (target-2)/2
		}else{
			target = (target-1)/2
		}
		res = append(res, target)
	}

	tmp := this.root
	for i:=len(res)-1;i>=0;i--{
		if tmp == nil{
			return false
		}
		if tmp.Val != res[i]{
			return false
		}
		if i==0{
			return true
		}
		if res[i-1]%2==0{
			tmp = tmp.Right
		}else{
			tmp = tmp.Left
		}
	}
	return true
}


/**
 * Your FindElements object will be instantiated and called as such:
 * obj := Constructor(root);
 * param_1 := obj.Find(target);
 */