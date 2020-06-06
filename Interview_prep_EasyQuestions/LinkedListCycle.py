https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/773/
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        slow = fast = head
        
        while fast and fast.next:
            
            slow = slow.next
            
            fast = fast.next.next
            
            if slow == fast:
                
                return True
        
        return False
        
        
