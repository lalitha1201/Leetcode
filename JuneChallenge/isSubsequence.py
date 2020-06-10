class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        left_len,right_len = len(s),len(t)
        
        i = j = 0
        
        while i < left_len and j < right_len:
            
            if s[i] == t[j]:
                
                i += 1
            
            j += 1
            
        
        return i == left_len
        
        
        
