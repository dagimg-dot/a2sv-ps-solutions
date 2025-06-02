# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = [(root, 0)]
        current_value = 0
        current_index = 0

        while queue:
            root, index = queue.pop(0)
            if index % 2 == 0:
                if root.val % 2 == 0:
                    return False
                if index == current_index and root.val <= current_value:
                    return False
            else:
                if root.val % 2 != 0:
                    return False
                if index == current_index and root.val >= current_value:
                    return False

            current_index = index
            current_value = root.val

            if root.left:
                queue.append((root.left, index + 1))
            if root.right:
                queue.append((root.right, index + 1))

        return True
