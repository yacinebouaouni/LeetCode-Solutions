# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def flat(node):
            if not node:
                return

            if not node.right and not node.left:
                return node

            elif not node.right:
                node.right = flat(node.left)
                node.left = None
                return node

            elif not node.left:
                node.right = flat(node.right)
                return node

            else:
                tmpRight = node.right
                node.right = flat(node.left)
                tmp = node.right
                while tmp.right:
                    tmp = tmp.right
                tmp.right = flat(tmpRight)
                node.left = None
                return node

        flat(root)
        