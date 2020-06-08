https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3349/
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        costs.sort(key = lambda x: x[0] - x[1])
        
        min_cost = 0
        
        n = len(costs) // 2
        
        for i in range(n):
            
            min_cost += costs[i][0] + costs[i+n][1]
        
        return min_cost
            
        
