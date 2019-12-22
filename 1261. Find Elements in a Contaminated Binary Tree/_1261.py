# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class FindElements:
    def __init__(self, root: TreeNode):
        if root:
            root.val = 0
            self.recover(root)
        self.root = root

    def recover(self, root: TreeNode):
        if root.left:
            root.left.val = root.val*2+1
            if root.left.left or root.left.right:
                self.recover(root.left)
        if root.right:
            root.right.val = root.val*2+2
            if root.right.left or root.right.right:
                self.recover(root.right)

    def find(self, target: int) -> bool:
        res = list()
        res.append(target)
        while target!=0:
            if target % 2 == 1:
                target = (target-1)/2
                res.append(target)
            else:
                target = (target-2)/2
                res.append(target)
        res.reverse()
        root = self.root
        for i in range(len(res)):
            if not root:
                return False
            if root.val != res[i]:
                return False
            if i == len(res)-1:
                return True
            if res[i+1]%2 == 0:
                root = root.right
            else:
                root = root.left

class FindElements1:
    def __init__(self, root: TreeNode):
        self.seen = set()
        
        def dfs(node: TreeNode, v: int) -> None:
            if node:
                node.val = v    
                self.seen.add(v)
                dfs(node.left, 2 * v + 1)
                dfs(node.right, 2 * v + 2)
            
        dfs(root, 0)
        
    def find(self, target: int) -> bool:
        return target in self.seen


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)