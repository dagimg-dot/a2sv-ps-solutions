class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        distance = [[0 for j in range(n)] for i in range(m)]
        visited = [[0 for j in range(n)] for i in range(m)]
        q = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    visited[i][j] = 1
                    q.append([i, j, 0])

        while len(q) > 0:
            a, b, dis = q.popleft()
            for r, c in [(a, b - 1), (a, b + 1), (a - 1, b), (a + 1, b)]:
                if 0 <= r < m and 0 <= c < n and visited[r][c] == 0:
                    visited[r][c] = 1
                    distance[r][c] = dis + 1
                    q.append([r, c, distance[r][c]])
                    
        return distance
