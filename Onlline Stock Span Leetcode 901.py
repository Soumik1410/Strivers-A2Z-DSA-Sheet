class StockSpanner:

    def __init__(self):
        self.stack  = []
        self.spans = []
        

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1] <= price:
            span += self.spans[-1]
            self.stack.pop()
            self.spans.pop()
        self.stack.append(price)
        self.spans.append(span)
        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
