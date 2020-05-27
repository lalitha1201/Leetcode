class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        # Hash table implementation
        
        counter_p = Counter(p); n = len(s); m = len(p); array = []
        for i in range(n-m+1):
            counter_s = Counter(s[i:i+m])
            if counter_s == counter_p: array.append(i)
        return array    
            
            
