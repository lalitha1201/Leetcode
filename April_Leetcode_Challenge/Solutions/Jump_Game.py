class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        target = len(nums)
        
        max_jump = 0
        
        i = 0
        
        while i <= max_jump:
            
            max_jump = max(nums[i]+i , max_jump)
            
            i += 1
            
            if i >= target:
                
                return True
        
        return False
            
            
