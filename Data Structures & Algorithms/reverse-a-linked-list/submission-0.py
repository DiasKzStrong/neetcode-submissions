# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        head_tmp = head
        head_next_tmp = head.next
        head.next = None
        head = head_next_tmp

        while head:
            head_next_tmp = head.next
            head.next = head_tmp
            head_tmp = head
            head = head_next_tmp
            
        return head_tmp