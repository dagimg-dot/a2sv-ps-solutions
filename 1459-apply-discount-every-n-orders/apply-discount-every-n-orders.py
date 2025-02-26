class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.disc = discount
        self.hash_map = defaultdict(int)
        for i in range(len(products)):
            self.hash_map[products[i]] = prices[i]
        self.ctr = 0        

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.ctr += 1
        bill = 0
        for i in range(len(product)):
            bill += self.hash_map[product[i]] * amount[i]
        if (self.ctr % self.n == 0):
            disc = (self.disc/100) * bill
            bill -= disc
        return bill  


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)