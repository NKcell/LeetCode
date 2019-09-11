def findMode(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if root is None:
        return []

    tree = [root]
    tree_value = {}
    while tree:
        temp = tree.pop()
        try:
            tree_value[str(temp.val)] += 1
        except:
            tree_value[str(temp.val)] = 1

        if temp.left is not None:
            tree.append(temp.left)
        if temp.right is not None:
            tree.append(temp.right)

    max_value = 0

    for key in tree_value:
        if tree_value[key] > max_value:
            max_value = tree_value[key]

    max_root = []
    for key in tree_value:
        if tree_value[key] == max_value:
            max_root.append(int(key))

    return max_root


"""
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.max = 0
        self.ctr = -1
        self.pre = None
        self.output = []
		
        self.traverse(root)
        self.update()
		
        return self.output
    
    def update(self):
        if self.ctr > self.max:
            self.output = [self.pre]
            self.max = self.ctr
        elif self.ctr == self.max:
            self.output.append(self.pre)
        
    def traverse(self, root):
        if root == None:
            return
        
        self.traverse(root.left)    
        
        if root.val == self.pre:
            self.ctr += 1
        else:
            self.update()
            self.ctr = 1
            self.pre = root.val
        
        self.traverse(root.right)
"""