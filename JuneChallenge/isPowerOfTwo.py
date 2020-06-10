class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        # O(1) approach
        
        if n == 0:
            
            return False
        
        return n & (n-1) == 0
