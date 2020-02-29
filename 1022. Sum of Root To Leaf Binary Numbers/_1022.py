# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        res = list()
        if root:
            self.getValue(root, root.val, res)
        return sum(res)

    def getValue(self, root, value, res):
        if not root.left and not root.right:
            res.append(value)
            return
        value *= 2
        if root.left:
            self.getValue(root.left, value+root.left.val, res)
        if root.right:
            self.getValue(root.right, value+root.right.val, res)