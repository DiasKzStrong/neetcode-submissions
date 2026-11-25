# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = True

        def dfs(root, left, right):
            nonlocal res 

            if not root:
                return

            if not (left < root.val < right):
                res = False
                return 
            
            dfs(root.left, left, root.val)
            dfs(root.right, root.val, right)

        dfs(root, float('-inf'), float('inf'))

        return res
        