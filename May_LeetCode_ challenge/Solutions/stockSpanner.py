class StockSpanner:

    def __init__(self):
        
        self.stack = []
        

    def next(self, price: int) -> int:
        
        span_weight = 1
        
        while self.stack and self.stack[-1][0] <= price:
            
            prev_price,prev_span = self.stack.pop()
            
            span_weight += prev_span
        
        
        self.stack.append((price,span_weight))
        
        return span_weight
        
