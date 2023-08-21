# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, count, sup):

            if not root:
                return count

            if root.val >= sup:
                sup = root.val
                count += 1

            count = dfs(root.left, count, sup) 
            count = dfs(root.right, count, sup)

            return count

        return dfs(root, 0, root.val)
            