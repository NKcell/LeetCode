# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        res = list()
        self.inorder(root, res)
        res.reverse()
        tmp = None
        for i in res:
            tmp1 = TreeNode(i)
            tmp1.right = tmp
            tmp = tmp1
        return tmp

    def inorder(self, root, res):
        if root.left:
            self.inorder(root.left, res)
        res.append(root.val)
        if root.right:
            self.inorder(root.right, res)

    def increasingBST1(self, root, tail = None):
        if not root: return tail
        res = self.increasingBST1(root.left, root)
        root.left = None
        root.right = self.increasingBST1(root.right, tail)
        return res