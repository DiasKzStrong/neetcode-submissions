# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_depth = self.findMaxDepth(root)

        return max_depth - 1

    def findMaxDepth(self, root, depth=1):
        if not root:
            return depth

        depth += 1

        left = self.findMaxDepth(root.left,depth)
        right = self.findMaxDepth(root.right, depth)

        return left if left > right else right

        