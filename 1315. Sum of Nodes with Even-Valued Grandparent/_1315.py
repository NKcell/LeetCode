# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        res = [0]
        self.grand(root, res)
        return res[0]

    def grand(self, root, res):
        if root.val%2 == 0:
            if root.left:
                self.parent(root.left, res)
            if root.right:
                self.parent(root.right, res)
    
        if root.left:
            self.grand(root.left, res)
        if root.right:
            self.grand(root.right, res)

    def parent(self, root, res):
        if root.left:
            res[0]+=root.left.val
        if root.right:
            res[0]+=root.right.val

    def sumEvenGrandparent1(self, root, p=1, gp=1):
        return self.sumEvenGrandparent1(root.left, root.val, p) \
            + self.sumEvenGrandparent1(root.right, root.val, p) \
            + root.val * (1 - gp % 2) if root else 0