# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isSameTree(p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    if p is None and q is None:
        return True
    if p is None and q is not None:
        return False
    if p is not None and q is None:
        return False

    res_p = []
    res_q = []

    perb(p, res_p)
    perb(q, res_q)

    print(res_p)
    print(res_q)

    if res_q == res_p:
        return True
    else:
        return False



def perb(p, res):
    res.append(p.val)
    if p.left is not None:
        perb(p.left, res)
    if p.left is None and p.right is not None:
        res.append('null')

    if p.right is not None:
        perb(p.right,res)


q = TreeNode(10)
q.right = TreeNode(15)
q.left = TreeNode(5)

p = TreeNode(10)
p.left = TreeNode(5)
p.left.right = TreeNode(15)

print(isSameTree(p, q))







