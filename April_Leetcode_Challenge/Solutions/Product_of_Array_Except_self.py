class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        length = len(nums)
        
        L , R , output = [0] * length , [0] * length , [0] * length
        
        
        # Lets findout left most product
        
        # Since Array starts with 0th element,there is -1th element
        
        L[0] = 1
        
        for i in range(1,length):
            
            L[i] = nums[i-1] * L[i-1]
            
        
        #Lets findout Right most product
        
        R[length - 1] = 1
        
        for i in reversed(range(length - 1)):
            
            R[i] = nums[i+1] * R[i+1]
            
        
        for i in range(length):
            
            output[i] = L[i] * R[i]
            
        
        
        return output
    
        
        
