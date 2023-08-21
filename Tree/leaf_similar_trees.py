# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:


        def inorder(root, leafs):

            if not root:
                return

            if not root.left and not root.right:
                leafs.append(root.val)
                return

            inorder(root.left, leafs)
            inorder(root.right, leafs)

        leafs1, leafs2 = [], []
        inorder(root1, leafs1)
        inorder(root2, leafs2)

        return leafs1 == leafs2
    