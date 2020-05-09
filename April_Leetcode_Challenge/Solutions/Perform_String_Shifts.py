class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        
        n = len(s)
        
        total_shift = 0
        
        for direction,amount in shift:
            
            if direction == 0:
                
                total_shift += amount
            
            else:
                
                total_shift = total_shift - amount
                
        total_shift = total_shift % n 
        
        return s[total_shift:] + s[:total_shift]
        
