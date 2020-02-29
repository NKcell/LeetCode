# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        num = 0
        res = list()
        self.getson(root, res, num)
        ressum = 0
        for i in res:
            ressum += i[0]
        return ressum

    def getson(self, root, res, num):
        num += 1
        if root.right is None and root.left is None:
            if len(res) != 0:
                if num > res[0][1]:
                    res[:] = []
                    res.append([root.val, num])
                elif num == res[0][1]:
                    res.append([root.val, num])
            else:
                res.append([root.val, num])

        else:
            if root.right is not None:
                self.getson(root.right, res, num)
            if root.left is not None:
                self.getson(root.left, res, num)

a1 = TreeNode(38)
a2 = TreeNode(43)
a3 = TreeNode(70)
a1.right = a2
a1.left = a3
a4 = TreeNode(16)
a2.left = a4
a5 = TreeNode(78)
a6 = TreeNode(91)
a3.left = a5
a3.right = a6
a7 = TreeNode(71)
a4.right = a7
a8 = TreeNode(27)
a5.left = a8
a9 = TreeNode(71)
a6.left = a9
a10 = TreeNode(71)
a8.left = a10
a = Solution()
# 38
# 43      70
# 16      78      91
# 71      27      71
#         71
print(a.deepestLeavesSum(a1))