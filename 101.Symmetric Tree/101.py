# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.isRverse(root.left, root.right)

    def isRverse(self, p, q):
        if p is None and q is None:
            return True
        if p is None and q is not None:
            return False
        if p is not None and q is None:
            return False
        return p.val == q.val and self.isRverse(p.left, q.right) and self.isRverse(p.right, q.left)
