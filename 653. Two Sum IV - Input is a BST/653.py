def findTarget(self, root, k):
    """
    :type root: TreeNode
    :type k: int
    :rtype: bool
    """
    if root is None:
        return False

    value_list= []
    root_list = [root]

    while root_list:
        temp = root_list.pop()

        value_list.append(temp.val)
        if temp.left is not None:
            root_list.append(temp.left)
        if temp.right is not None:
            root_list.append(temp.right)

    for i in value_list:
        if k-i != i and k-i in value_list:
            return True

    return False

"""
if not root:
            return False
        s = set()
        q = collections.deque([root])
        while q:
            n = q.popleft()
            if n:
                if k - n.val in s:
                    return True
                s.add(n.val)
                q.append(n.left)
                q.append(n.right)                
        return False

"""