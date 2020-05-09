class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        def backspace(S):
            
            c = []
            
            for char in S:
                
                if char != '#':
                    
                    c.append(char)
                
                elif c:
                    
                    c.pop()
                
            return "".join(c)
                
      
        if backspace(S) == backspace(T) :
            
            return True
        
        else:
            
            return False
                    
