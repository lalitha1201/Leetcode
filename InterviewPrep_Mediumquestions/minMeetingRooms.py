https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/805/
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start_times = sorted(i[0] for i in intervals)
        
        end_times = sorted(i[1] for i in intervals)
        
        
        result = len(intervals)
        
        for i in start_times:
            
            for j in end_times:
                
                if j <= i :
                    
                    result -= 1
                    
                    end_times.remove(j)
                    
                    break
        
        return result
        
