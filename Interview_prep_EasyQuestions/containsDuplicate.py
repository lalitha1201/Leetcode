#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/578/
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        counter_dup = collections.Counter(nums)
        
        for x,y in counter_dup.items():
            
            if y != 1:
                
                return True
        
        return False
        
