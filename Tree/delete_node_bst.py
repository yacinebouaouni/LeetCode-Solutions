# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if root is None:
            return None

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)

        else:

            if not root.left and not root.right:
                return None

            if not root.left:
                replace = root.right
                root = None
                return replace

            if not root.right:
                replace = root.left
                root = None
                return replace

            if root.right and root.left:
                replace = self.get_min(root.right)
                root.val = replace.val
                root.right = self.deleteNode(root.right, replace.val)
                print(replace)
    

        return root


    
    def get_min(self, node):

        while node.left:
            node = node.left
        
        return node