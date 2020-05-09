class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x: int) -> None:
        
        if not self.stack:
            
            self.stack.append((x,x))
            
            return
            
        minimum = self.stack[-1][1]
        
        self.stack.append((x,min(x,minimum)))
        
        
        
        

    def pop(self) -> None:
        
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        
