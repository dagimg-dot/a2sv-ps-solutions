class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = [0] * n
        for i, j in edges:
            indegree[j] += 1
        ans = []
        for i in range(n):
            if indegree[i] == 0:
                ans.append(i)

        return ans
