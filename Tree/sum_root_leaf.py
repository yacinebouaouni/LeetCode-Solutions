# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def root_leaf(node, currtot):
            if not node:
                return 0
            
            currtot = currtot * 10 + node.val
            if not node.left and not node.right:
                return currtot

            left_sum = root_leaf(node.left, currtot)
            right_sum = root_leaf(node.right, currtot)
            
            return left_sum + right_sum
        
        return root_leaf(root, 0)
