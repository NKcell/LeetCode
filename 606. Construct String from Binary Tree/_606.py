# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        res = list()
        if not t:
            return ""
        res.append(str(t.val))
        if t.left or t.right:
            self.tree(t.left, res)
            if t.right:
                self.tree(t.right,res)
        return ''.join(res)


    def tree(self, t: TreeNode, res: list):
        if not t:  
            res.append('()')
        else:
            res.append('(')
            res.append(str(t.val))
            if t.right or t.left:
                self.tree(t.left, res)
                if t.right:
                    self.tree(t.right,res)
            res.append(')')

    def tree2str1(self, t):
        if not t: return ''
        left = '({})'.format(self.tree2str(t.left)) if (t.left or t.right) else ''
        right = '({})'.format(self.tree2str(t.right)) if t.right else ''
        return '{}{}{}'.format(t.val, left, right)

    def tree2str2(self, t):
        if t is None:
                return ""
        ans = str(t.val) 
        if t.left:
            ans+="(" + self.tree2str(t.left) + ")"
        if not t.left and t.right:
            ans+="()"
        if t.right:
            ans+="(" + self.tree2str(t.right) + ")"
        return ans