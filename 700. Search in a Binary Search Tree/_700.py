# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def searchBST1(self, root: TreeNode, val: int) -> TreeNode:
        return self.getNode(root, val)

    def getNode(self, root, val):
        if root is None:
            return None
        if val == root.val:
            return root
        if val>root.val:
            return self.getNode(root.right, val)
        if val<root.val:
            return self.getNode(root.left, val)

    def searchBST(self, root, val):
        if root and val < root.val: return self.searchBST(root.left, val)
        elif root and val > root.val: return self.searchBST(root.right, val)
        return root