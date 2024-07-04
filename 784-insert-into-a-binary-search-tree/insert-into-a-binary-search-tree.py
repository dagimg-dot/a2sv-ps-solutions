# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        new_treeNode = TreeNode(val)
        if root == None:
            root = new_treeNode
        else:
            parent = None
            current = root
            while current != None:
                if val < current.val:
                    parent = current
                    current = current.left
                elif val > current.val:
                    parent = current
                    current = current.right
                else:
                    return False

            if val < parent.val:
                parent.left = new_treeNode
            else:
                parent.right = new_treeNode
        
        return root
