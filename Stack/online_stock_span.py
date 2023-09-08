class StockSpanner:

    def __init__(self):
        self.stack = []
        self.idx = 0
        

    def next(self, price: int) -> int:
        
        while self.stack and price >= self.stack[-1][0]:
            self.stack.pop()

        self.stack.append((price, self.idx))
        self.idx += 1

        if len(self.stack)>1:
            return self.stack[-1][1]-self.stack[-2][1]
        else:
            return self.idx
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)