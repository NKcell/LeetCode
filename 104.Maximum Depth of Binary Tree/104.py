# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        height = 0
        h = self.cal_height(height, root)
        return h

    def cal_height(self, h, p):
        if p is None:
            return h

        h += 1
        return max(self.cal_height(h, p.left), self.cal_height(h, p.right))