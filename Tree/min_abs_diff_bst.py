# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        prev, minDiff = float('-inf'), float('inf')

        def inorder(node):
            nonlocal prev, minDiff
            
            if not node:
                return

            if node.left:
                inorder(node.left)
            
            minDiff = min(minDiff, abs(node.val-prev))
            prev = node.val

            if node.right:
                inorder(node.right)
        
        inorder(root)
        return minDiff
