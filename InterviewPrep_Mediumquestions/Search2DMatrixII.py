https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/806/
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0  or len(matrix[0]) == 0:
            return False
        
        height = len(matrix)
        width = len(matrix[0])
        
        rows = height - 1
        
        columns = 0
        
        while rows >= 0 and columns < width:
            
            if matrix[rows][columns] > target:
                rows -= 1
                
            elif matrix[rows][columns] < target:
                columns += 1
                
            else:
                return True
            
        return False
    
