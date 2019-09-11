class Solution:
    def intersect(self, quadTree1, quadTree2):
        """
        :type quadTree1: Node
        :type quadTree2: Node
        :rtype: Node
        """
        if quadTree1.isLeaf == True :
            node = quadTree1
            node.val = quadTree1.val or quadTree2.val
            return node

        if quadTree2.isLeaf == True :
            node = quadTree2
            node.val = quadTree1.val or quadTree2.val
            return node

        node = quadTree1
        node.isLeaf = False
        tl = self.creattree(quadTree1.topLeft, quadTree2.topLeft, node.topLeft)
        tr = self.creattree(quadTree1.topRight, quadTree2.topRight, node.topRight)
        bl = self.creattree(quadTree1.bottomLeft, quadTree2.bottomLeft, node.bottomLeft)
        br = self.creattree(quadTree1.bottomRight, quadTree2.bottomRight, node.bottomRight)
        if tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf and tl.val == tr.val == bl.val == br.val:
            node.val = tl.val
        else:
            node.val = False

        return node


    def creattree(self, quadTree1, quadTree2, node):
        if quadTree1.isLeaf == True:
            if quadTree1.val == True:
                node = quadTree1
            else:
                node = quadTree2
            return node

        if quadTree2.isLeaf == True:
            if quadTree2.val == True:
                node = quadTree2
            else:
                node = quadTree1
            return node

        node.val = quadTree1.val or quadTree2.val
        node.isLeaf = False
        tl = self.creattree(quadTree1.topLeft, quadTree2.topLeft, node.topLeft)
        tr = self.creattree(quadTree1.topRight, quadTree2.topRight, node.topRight)
        bl = self.creattree(quadTree1.bottomLeft, quadTree2.bottomLeft, node.bottomLeft)
        br = self.creattree(quadTree1.bottomRight, quadTree2.bottomRight, node.bottomRight)
        if tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf and tl.val == tr.val == bl.val == br.val:
            node.val = tl.val
        else:
            node.val = False
        return node


# 只有下面这个是对的
class Solution:
    def intersect(self, q1, q2):
        if q1.isLeaf:
            return q1.val and q1 or q2
        elif q2.isLeaf:
            return q2.val and q2 or q1
        else:
            tLeft = self.intersect(q1.topLeft, q2.topLeft)
            tRight = self.intersect(q1.topRight, q2.topRight)
            bLeft = self.intersect(q1.bottomLeft, q2.bottomLeft)
            bRight = self.intersect(q1.bottomRight, q2.bottomRight)
            if tLeft.isLeaf and tRight.isLeaf and bLeft.isLeaf and bRight.isLeaf and tLeft.val == tRight.val == bLeft.val == bRight.val:
                node = Node(tLeft.val, True, None, None, None, None)
            else:
                node = Node(False, False, tLeft, tRight, bLeft, bRight)
        return node



"""
class Solution:
    def intersect(self, quadTree1, quadTree2):

        if quadTree1.isLeaf == True :
            node = quadTree1
            node.val = quadTree1.val or quadTree2.val
            return node
        
        if quadTree2.isLeaf == True :
            node = quadTree2
            node.val = quadTree1.val or quadTree2.val
            return node
        
        node = quadTree1
        node.val = quadTree1.val or quadTree2.val
        node.isLeaf = False
        self.creattree(quadTree1.topLeft, quadTree2.topLeft, node.topLeft)
        self.creattree(quadTree1.topRight, quadTree2.topRight, node.topRight)
        self.creattree(quadTree1.bottomLeft, quadTree2.bottomLeft, node.bottomLeft)
        self.creattree(quadTree1.bottomRight, quadTree2.bottomRight, node.bottomRight)
        
        return node
        
        
    def creattree(self, quadTree1, quadTree2, node):
        if quadTree1.isLeaf == True:
            if quadTree1.val == True:
                node = quadTree1
            else:
                node = quadTree2
            return node

        if quadTree2.isLeaf == True:
            if quadTree2.val == True:
                node = quadTree2
            else:
                node = quadTree1
            return node

        node.val = quadTree1.val or quadTree2.val
        node.isLeaf = False
        self.creattree(quadTree1.topLeft, quadTree2.topLeft, node.topLeft)
        self.creattree(quadTree1.topRight, quadTree2.topRight, node.topRight)
        self.creattree(quadTree1.bottomLeft, quadTree2.bottomLeft, node.bottomLeft)
        self.creattree(quadTree1.bottomRight, quadTree2.bottomRight, node.bottomRight)

"""

