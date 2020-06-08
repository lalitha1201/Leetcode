https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3350/
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        
        """
        n = len(s) -1
        for i in range(len(s)//2):
            
            s[i],s[n] = s[n],s[i]
            
            n -= 1
        
        return s
