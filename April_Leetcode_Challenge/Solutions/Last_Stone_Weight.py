class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones.sort()
        
        while len(stones) > 1:
            
            
            
            x = stones.pop()
                
            y = stones.pop()
            
            
            if x != y :
                
                bisect.insort(stones,x - y)
                
            
        return stones[0] if stones else 0    
