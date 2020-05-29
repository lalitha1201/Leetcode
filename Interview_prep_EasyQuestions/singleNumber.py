https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        from collections import Counter
        
        single_number = Counter(nums)
        
        for x,y in single_number.items():
            
            if y == 1:
                
                return x
