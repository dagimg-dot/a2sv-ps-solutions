# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        adj = defaultdict(list)
        vis = set()
        res = []

        def makeGraph(node):
            if node.left:
                adj[node].append(node.left)
                adj[node.left].append(node)
                makeGraph(node.left)
            if node.right:
                adj[node].append(node.right)
                adj[node.right].append(node)
                makeGraph(node.right)

        makeGraph(root)

        def dfs(node, d):
            if d < k:
                vis.add(node)
                d += 1
                for u in adj[node]:
                    if u not in vis:
                        dfs(u, d)
            else:
                res.append(node.val)

        dfs(target, 0)
        return res
