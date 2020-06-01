https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/799/
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter_nums = collections.Counter(nums)
        
        return [key for key,_ in counter_nums.most_common(k)]
        
