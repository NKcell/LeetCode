class ProductOfNumbers:

    def __init__(self):
        self.mylist = list()
        self.last0 = -1

    def add(self, num: int) -> None:
        if num == 0:
            self.last0 = len(self.mylist)+1
        if not self.mylist or self.mylist[-1] == 0:
            self.mylist.append(num)
        else:
            self.mylist.append(self.mylist[-1]*num)
        

    def getProduct(self, k: int) -> int:
        if len(self.mylist)-k+1 <= self.last0:
            return 0
        else:
            if len(self.mylist) == k:
                return self.mylist[-1]

            if self.mylist[len(self.mylist)-k-1] == 0:
                return self.mylist[-1]
            else:
                return self.mylist[-1]//self.mylist[len(self.mylist)-k-1]