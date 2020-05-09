class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        
        count_of_stones = collections.Counter(S)
        
        sum = 0
        
        for char in J:            
            if char in S:
                
                sum += count_of_stones[char]
                
        
        return sum 
