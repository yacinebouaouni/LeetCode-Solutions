# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:


        queue = deque([root])
        maxSum, min_level, curr_lvl = float('-inf'), 0, 0

        while queue:
            n = len(queue)
            currSum = 0
            curr_lvl += 1

            while n > 0 :
                node = queue.popleft()
                n -= 1
                currSum += node.val
                    
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)

            if currSum > maxSum:
                min_level = curr_lvl
                maxSum = currSum

        return min_level