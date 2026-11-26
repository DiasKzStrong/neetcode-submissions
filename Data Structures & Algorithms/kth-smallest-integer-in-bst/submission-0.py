# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import heapq

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nums = []

        q = deque([root])

        while q:
            node = q.popleft()
            nums.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        heapq.heapify(nums)

        for _ in range(k):
            smallest = heapq.heappop(nums)

        return smallest