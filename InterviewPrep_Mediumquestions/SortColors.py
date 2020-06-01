https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/798/
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        red = white = blue = 0
        
       
        
        for i in range(len(nums)):
            
            curr = nums[i]
            
            if curr <= 2:
                
                nums[blue] = 2
                
                blue += 1
                
            if curr <= 1:
                
                nums[white] = 1
                
                white += 1
                
            if curr <= 0:
                
                nums[red] = 0
                
                red += 1
                
