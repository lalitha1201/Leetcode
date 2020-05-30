class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        len_a = len_b = 0
        list_a = headA
        list_b = headB
		# Get the length of both linked lists
        while list_a:
            len_a += 1
            list_a = list_a.next
        while list_b:
            len_b += 1
            list_b = list_b.next
		# Move the head of the longest list on the same position(with short head) from the end.
        if len_a > len_b:
            for i in range(0, len_a-len_b):
                headA = headA.next
        else:
            for i in range(0, len_b-len_a):
                headB = headB.next
		# Move 2 pointers
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
