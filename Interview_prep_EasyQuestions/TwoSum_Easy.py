https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self,nums,target):
        
        dicti = {}
        
        for i , num in enumerate(nums):
            
            n = target - num
            
            if n not in dicti:
                
                dicti[num] = i
                
            else:
                
                return [dicti[n],i]
