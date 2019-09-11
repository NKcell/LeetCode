import queue
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dl = queue.Queue()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.dl.put(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        re = []
        while not self.dl.empty():
            re.append(self.dl.get())

        print (re)
        if len(re) == 0:
            res = None
        else:
            res = re[-1]
            re = re[:-1]
            for i in re:
                self.dl.put(i)
        return res

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        re = []
        while not self.dl.empty():
            re.append(self.dl.get())
        print(re)
        if len(re) == 0:
            res = None
        else:
            res = re[-1]

            for i in re:
                self.dl.put(i)
        return res

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.dl.empty()

l = MyStack()
l.push(1)

print(l.pop())
print (l.empty())