# https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/795/
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # BackTracking Problem
        
        output = []
        n = len(nums)
        
        def backtrack(first):
            
            if first == n:
                
                output.append(nums[:])
            
            for i in range(first,n):
                
                nums[first] , nums[i] = nums[i] ,nums[first]
                
                backtrack(first+1)
                
                
                nums[first] ,nums[i] = nums[i] ,nums[first]
            
            
            
        
        backtrack(0)
        
        return output
        
