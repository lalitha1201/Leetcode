https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) == 0 or len(prices) == 1:
            return 0
        
        min_price  = prices[0]
        profit = 0
        
        for i in range(1,len(prices)):
            
            if min_price > prices[i]:
                
                min_price = prices[i]
                
            else:
                
                profit = max(profit,prices[i] - min_price)
                
        
        
        return profit
                
                
            
            
            
           /
