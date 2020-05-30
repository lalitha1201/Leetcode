# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s):
        
        substring = []
        c = 0
        
        for x in s:
            
            if x in substring:
                
                substring = substring[substring.index(x) + 1:]
                
            substring.append(x)
                
            c = max(c,len(substring))
                
                
        
        return c
        
