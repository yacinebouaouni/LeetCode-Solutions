# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return root

        output = []
        def zigzag(node, left, level):

            if not node:
                return

            if len(output)<level:
                output.append(deque())
            
            if left:  
                output[level-1].appendleft(node.val)
            else:
                output[level-1].append(node.val)

            zigzag(node.left, not left, level+1)
            zigzag(node.right, not left, level+1)

        
        zigzag(root, False, 1)

        return output 