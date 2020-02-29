class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if len(self.stack)!=0:
            return self.stack[-1]
        return None

    def getMin(self) -> int:
        return min(self.stack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


# class MinStack(object):

#     def __init__(self):
#         self.stack = []
        
#     def push(self, x):
#         self.stack.append((x, min(self.getMin(), x))) 
           
#     def pop(self):
#         self.stack.pop()

#     def top(self):
#         if self.stack:
#             return self.stack[-1][0]
        
#     def getMin(self):
#         if self.stack:
#             return self.stack[-1][1]
#         return sys.maxint 