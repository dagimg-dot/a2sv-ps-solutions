# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        x = root.val

        def searchtree(node, value):
            if not node:
                return True
            if node.val != value:
                return False
            return searchtree(node.left, value) and searchtree(node.right, value)

        return searchtree(root, x)
