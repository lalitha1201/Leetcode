class Solution:
    def countElements(self, arr: List[int]) -> int:
        
        dict1 = {}
        
        count = 0
        
        for i in arr:
            
            dict1[i] = 1
        
        for x in arr:
            
            if x+1 in dict1:
                
                count += 1
        
        return count
                
