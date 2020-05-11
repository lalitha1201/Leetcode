class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        if num < 2:
            
            return True
        
        #Binary Search
        
        left,right = 2,num // 2
        
        while left <= right:
            
            mid = left + (right - left) // 2
            
            num_square = mid * mid 
            
            if num_square == num:
                
                return True
            
            elif num_square > num:
                
                right = mid - 1
                
            
            elif num_square < num:
                
                left = mid + 1
                
        
        return False
