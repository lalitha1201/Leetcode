class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        
        current = head
        c = 0
        
        while current:
            
            c += 1
            current = current.next
            
        if c == 1:
            return head
        
        current = head
        
        
        l = 0
        
        while current:
            
            l = l+1
            
            current = current.next
            
            if l == c//2 :
                
                return current
