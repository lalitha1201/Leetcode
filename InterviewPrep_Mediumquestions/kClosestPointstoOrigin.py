class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
       
        
        
        
        c = list()
        ans = list()
        
        for point in points:
            d = self.find_distance(point)
            heapq.heappush(c,(d,point))
        
        for _ in range(K):
            ans.append(heapq.heappop(c)[1])
            K-=1

        return ans
    def find_distance(self,point):
            return math.sqrt(point[0]**2 + point[1]**2)
                    
            
