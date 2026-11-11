# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:        
        curr = head
        prev_curr = None
        new_head = None

        while curr:
            cur = curr
            c = 0
            while cur and c < k:
                cur = cur.next    
                c += 1

            if c != k:
                break   
            
            prev2 = None
            cur = curr
            while cur and c != 0:
                tmp = cur.next
                cur.next = prev2
                prev2 = cur 
                cur = tmp
                c -= 1


            # Save the new head after the first reversal
            if new_head is None:
                new_head = prev2

            # Connect previous group to current group
            if prev_curr is not None:
                prev_curr.next = prev2

            # Connect current group's tail to remaining nodes
            curr.next = cur

            # Current group's tail becomes previous group's tail
            prev_curr = curr

            # Move to the next group
            curr = cur
        
        return new_head if new_head else head