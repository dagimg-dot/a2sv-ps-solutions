# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack = [(root, float('-inf'), float('inf'))]

        while stack:
            node, min_val, max_val = stack.pop()

            if not node:
                continue
            
            if not (min_val < node.val < max_val):
                return False
            
            stack.append((node.right, node.val, max_val))
            stack.append((node.left, min_val, node.val))

        return True