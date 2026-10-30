# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None

        while second:   
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp


        l, r = head, prev

        while r:
            tmp_l, tmp_r = l.next, r.next

            l.next = r
            r.next = tmp_l

            l = tmp_l
            r = tmp_r


            

        
        


        
            
        

        