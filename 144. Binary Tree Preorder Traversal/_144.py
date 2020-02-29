#Definition for a binary tree node.
class TreeNode:
   def __init__(self, x):
      self.val = x
      self.left = None
      self.right = None

class Solution:
   def preorderTraversal(self, root: TreeNode):
      res = list()
      self.preorder(root, res)
      return res

   def preorder(self, root, res):
      if root is not None:
            res.append(root.val)
            self.preorder(root.left, res)
            self.preorder(root.right, res)

   def preorderTraversal1(self, root):
      ret = []
      stack = [root]
      while stack:
         node = stack.pop()
         if node:
               ret.append(node.val)
               stack.append(node.right)
               stack.append(node.left)
      return ret