https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/submissions/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        c = []
        Found = False
        count = 0
        
        for index,num in enumerate(nums):
            
            if num == target:
                
                c.append(index)
                
        
        if len(c) == 0:
            
             return [-1,-1]
        
        else:
            
            return [c[0],c[-1]]
                
        
