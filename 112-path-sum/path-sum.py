# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        curr = 0

        def check(curr, root):
            if root is None:
                return False
            curr += root.val
            if curr == targetSum and not root.left and not root.right:
                return True
            return check(curr, root.left) or check(curr, root.right)

        return check(0, root)
