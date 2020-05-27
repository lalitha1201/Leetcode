class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # Hash table Implementation
        
        counter_p = Counter(s1); n = len(s2); m = len(s1); 
        for i in range(n-m+1):
            counter_s = Counter(s2[i:i+m])
            if counter_s == counter_p: return True
        return False    
            
        
