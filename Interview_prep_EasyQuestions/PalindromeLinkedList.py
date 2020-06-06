https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/772/
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        palindrome = []
        current = head
        
        if not head:
            return True
        
        while current:
            
            
            palindrome.append(current.val)
            
            current = current.next
            
        if palindrome == palindrome[::-1]:
            
            return True
        else:
            return False
            
