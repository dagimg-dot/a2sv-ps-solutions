class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [0] * n
        count = 0

        def dfs(i):
            for j in range(len(isConnected)):
                if isConnected[i][j] and visited[j] == 0:
                    visited[j] = 1
                    dfs(j)

        for i in range(n):
            if visited[i] == 0:
                count += 1
                visited[i] = 1
                dfs(i)

        return count
