# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None

        first = 0
        last = len(nums) - 1

        root = TreeNode(nums[(first + last) // 2])

        self.creatLtree(first, (first + last) // 2 - 1, root, nums)
        self.creatRtree((first + last) // 2 + 1, last, root, nums)

        return root

    def creatLtree(self, first, last, root, nums):
        if first <= last:
            root.left = TreeNode(nums[(first + last) // 2])
            self.creatLtree(first, (first + last) // 2 - 1, root.left, nums)
            self.creatRtree((first + last) // 2 + 1, last, root.left, nums)
        else:
            return

    def creatRtree(self, first, last, root, nums):
        if first <= last:
            root.right = TreeNode(nums[(first + last) // 2])
            self.creatLtree(first, (first + last) // 2 - 1, root.right, nums)
            self.creatRtree((first + last) // 2 + 1, last, root.right, nums)
        else:
            return
