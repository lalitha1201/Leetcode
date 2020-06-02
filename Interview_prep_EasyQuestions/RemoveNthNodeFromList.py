https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/603/
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        # Find the length of the List
        
        fast = slow = head
        
        for _ in range(n):
            fast = fast.next
            
        
        if not fast:
            return head.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
            
        slow.next = slow.next.next
        
        return head
            
