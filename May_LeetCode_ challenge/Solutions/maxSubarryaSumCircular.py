class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        
        # First Find the max_value using kadane algorithm
        
        k = self.kadane(A)
        
        csum = 0
        
        for i in range(len(A)):
            
            csum += A[i]
            
            A[i] = -A[i]
            
        
        csum = csum + self.kadane(A)
        
        if csum != 0 and csum > k:
            
            return csum
        
        else:
            
            return k
            
            
        
    def kadane(self,num):
        
        max_sum,total_sum = num[0],num[0]
        
        for i in num[1:]:
            
            total_sum = max(i,i+total_sum)
            
            max_sum = max(max_sum,total_sum)
            
        return max_sum
            
            
        
        
        
