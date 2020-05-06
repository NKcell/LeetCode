# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = list()
        tmp = list()

        self.dfs(res, tmp, sum, root)
        return res

    def dfs(self, res, tmp, sum, root):
        if not root:
            return

        sum -= root.val

        if sum == 0 and not root.left and not root.right:
            res.append(tmp+[root.val])
            return
        
        self.dfs(res, tmp+[root.val], sum, root.left)
        self.dfs(res, tmp+[root.val], sum, root.right)