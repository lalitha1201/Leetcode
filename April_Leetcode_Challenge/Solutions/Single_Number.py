class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        from collections import Counter
        
        single_number = Counter(nums)
        
        for x,y in single_number.items():
            
            if y == 1:
                
                return x
