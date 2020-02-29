# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findFrequentTreeSum(self, root: TreeNode):
        if not root:
            return []

        mydict = dict()
        self.dfs(root, mydict)
        
        list1= sorted(mydict.items(),key=lambda x:x[1], reverse=True)
        
        flag = list1[0][1]
        
        reslist = list()
        for i in list1:
            if i[1] != flag:
                return reslist
            reslist.append(i[0])
        return reslist

    def dfs(self, root, mydict):
        while not root.left and not root.right:
            tmp = mydict.get(root.val, 0)
            mydict[root.val] = tmp+1
            return root.val
        tmp = 0
        if root.left:
            tmp += self.dfs(root.left, mydict)
        if root.right:
            tmp += self.dfs(root.right, mydict)

        dicttmp = mydict.get(root.val+tmp, 0)
        mydict[root.val+tmp] = dicttmp+1

        return root.val+tmp

    def findFrequentTreeSum1(self, root):
        import collections
        if root is None: return []

        def dfs(node):
            if node is None: return 0
            s = node.val + dfs(node.left) + dfs(node.right)
            count[s] += 1
            return s

        count = collections.Counter()
        dfs(root)
        maxCount = max(count.values())
        return [s for s in count if count[s] == maxCount]