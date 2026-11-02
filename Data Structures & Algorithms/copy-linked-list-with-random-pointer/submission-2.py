"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None
        curr = head 

        while curr:
            node = Node(curr.val, curr.next)
            tmp = curr.next
            curr.next = node 
            curr = tmp 

        newHead = head.next

        l1 = head
        while l1:
            if l1.random:
                l1.next.random = l1.random.next
            l1 = l1.next.next

        l1 = head
        while l1:
            l2 = l1.next
            l1.next = l2.next
            if l2.next:
                l2.next = l2.next.next
            l1 = l1.next

        return newHead

            