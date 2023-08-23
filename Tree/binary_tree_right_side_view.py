# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        output = [root.val]
        queue = deque([(root,0)])
        target = 1

        while queue:
            
            node, level = queue.popleft()
            if level == target:
                output.append(node.val)
                target += 1

            if node.right:
                queue.append((node.right, level+1))

            if node.left:
                queue.append((node.left, level+1))


        return output

