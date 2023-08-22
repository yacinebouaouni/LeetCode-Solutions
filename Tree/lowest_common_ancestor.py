# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.lci = None
        
        def dfs(node):
            if not node:
                return False, False
            
            left_p, left_q = dfs(node.left)
            right_p, right_q = dfs(node.right)
            
            current_p = left_p or right_p or node == p
            current_q = left_q or right_q or node == q
            
            if current_p and current_q and not self.lci:
                self.lci = node
                
            return current_p, current_q
        
        dfs(root)
        return self.lci
