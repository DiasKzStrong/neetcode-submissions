# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        head = dummy

        remainder = 0

        while l1 or l2:
            if l1 and l2:
                val = l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            elif l1:
                val = l1.val
                l1 = l1.next
            else:
                val = l2.val
                l2 = l2.next
            
            if remainder:
                val += remainder
                remainder = 0

            if val > 9:
                val = val - 10
                remainder = 1
        
            head.next = ListNode(val)
            head = head.next

        if remainder:
            head.next = ListNode(remainder)
    
        return dummy.next
