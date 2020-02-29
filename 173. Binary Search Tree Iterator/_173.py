# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.res = list()
        self.getNode(root)
        self.index = 0

    def getNode(self, root):
        if root == None:
            return
        if root.left:
            self.getNode(root.left)
        self.res.append(root.val)
        if root.right:
            self.getNode(root.right)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        if self.index<len(self.res):
            tmp = self.res[self.index]
            self.index += 1
            return tmp

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.index<len(self.res):
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()