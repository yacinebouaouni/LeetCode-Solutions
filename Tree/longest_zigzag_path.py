# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        self.maxLen = 0
        if not root.right and not root.left:
            return 0

        def dfs(node, currlen, direction):

            if node == None:
                return

            self.maxLen = max(currlen, self.maxLen)
    
    
            if direction == 'left':
                dfs(node.left, 1, 'left')
                dfs(node.right, currlen+1, 'right')

            elif direction == 'right':
                dfs(node.right, 1, 'right')
                dfs(node.left, currlen+1, 'left')

            else:
                dfs(node.left, currlen+1, 'left')
                dfs(node.right, currlen+1, 'right')


        dfs(root, 0, 0)
        return self.maxLen
