https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/796/
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        output = [[]]
        
        for num in nums:
            
            output += [curr + [num] for curr in output]
            
        
        return output
            
