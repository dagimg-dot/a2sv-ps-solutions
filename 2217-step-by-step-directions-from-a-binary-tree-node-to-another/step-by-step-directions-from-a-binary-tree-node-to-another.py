# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(
        self, root: Optional[TreeNode], startValue: int, destValue: int
    ) -> str:
        leftPath, rightPath = "", ""
        is_left, is_right = False, False
        st = [[root, ""]]

        while len(st) > 0 and (not is_left or not is_right):
            node, curr = st.pop()
            if node.val == startValue:
                leftPath = curr
                is_left = True
                print("reach start")
            if node.val == destValue:
                rightPath = curr
                print("reach dest")
                is_right = True
            if node.left:
                st.append([node.left, curr + "L"])
            if node.right:
                st.append([node.right, curr + "R"])

        i, j = 0, 0
        n, m = len(leftPath), len(rightPath)
        while i < n and j < m:
            if leftPath[i] == rightPath[j]:
                i += 1
                j += 1
            else:
                break

        return "U" * (n - i) + rightPath[j:]
