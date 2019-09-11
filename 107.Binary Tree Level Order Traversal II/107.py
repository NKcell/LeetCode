# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []

        if root is None:
            return res

        res = [[root.val]]
        tem = [root]

        while len(tem)!= 0:
            tem2 = []
            l = len(tem)
            for i in range(len(tem)):
                if tem[i].left is not None:
                    tem.append(tem[i].left)
                    tem2.append(tem[i].left.val)
                if tem[i].right is not None:
                    tem.append((tem[i].right))
                    tem2.append(tem[i].right.val)
            if len(tem2) != 0:
                res.append(tem2)
            tem = tem[l:]

        return list(reversed(res))