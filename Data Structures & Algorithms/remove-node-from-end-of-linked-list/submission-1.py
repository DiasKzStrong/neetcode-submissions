# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0

        curr = head
        while curr:
            curr = curr.next
            length += 1 

        ix = 0
        n = length - n

        curr, prev = head, ListNode()
        while curr:
            if ix == n:
                prev.next = curr.next
                if ix == 0:
                    head = prev.next
                break
            prev = curr
            curr = curr.next
            ix += 1
        
        return head