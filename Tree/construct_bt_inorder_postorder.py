# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_map={val:idx for idx, val in enumerate(inorder)}
        def recursive(inorder_idx, postorder_idx):
            if inorder_idx>postorder_idx:
                return None  # Base case: empty inorder list means an empty subtree

            # Create a new node using the last element of postorder
            node_val = postorder[postorder_idx]
            node = TreeNode(val=node_val)


            # Find the index of the node value in inorder list
            index = inorder_map[node_val]

            # Recursively build right and left subtrees
            node.right = recursive(inorder_idx + 1, postorder_idx)
            node.left = recursive(inorder[:index], postorder)

            return node

        return recursive(inorder, postorder)  # Reverse postorder list before starting
