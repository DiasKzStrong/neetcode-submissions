# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l = 0 
        storage = []

        curr = head

        while curr:
            storage.append(curr)
            curr = curr.next


        l, r  = 0, len(storage) - 1

        while l < r:
            l_node = storage[l]
            tmp_next = l_node.next

            r_node = storage[r]

            l_node.next = r_node
            r_node.next = tmp_next

            r -= 1
            l += 1

        storage[l].next = None

        
            
        

        