class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.myDict = dict()
        for i in range(len(products)):
            self.myDict[products[i]] = prices[i]
        self.npeople = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.npeople += 1
        if self.npeople == self.n:
            self.npeople = 0
            return sum([i[1]*self.myDict[i[0]] for i in zip(product, amount)]) *(1-self.discount/100)   
        else:
            return  sum([i[1]*self.myDict[i[0]] for i in zip(product, amount)])*1.0
        


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)