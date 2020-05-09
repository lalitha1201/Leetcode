class Solution:
    def checkValidString(self, s: str) -> bool:
        
        
        length = len(s)
        o = c = 0
        
        for i in range(length):
            
            if s[i] == '*' or s[i] == '(':
                
                o += 1
            
            else:
                
                o -= 1
        
            if s[length-i-1] == '*' or s[length-i-1] == ')':
                
                c += 1
            
            else:
                
                c -= 1
                
            if o < 0 or c < 0:
                
                return False
        
        
        return True
                
