class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        queue = deque([(*entrance, 0)])
        visited = [[False] * n for _ in range(m)]
        visited[entrance[0]][entrance[1]] = True

        while queue:
            i, j, level = queue.popleft()

            if (i in {0, m - 1} or j in {0, n - 1}) and [i, j] != entrance:
                return level

            for x, y in directions:
                x, y = x + i, y + j
                if (
                    0 <= x < m
                    and 0 <= y < n
                    and not visited[x][y]
                    and maze[x][y] == "."
                ):
                    queue.append((x, y, level + 1))
                    visited[x][y] = True

        return -1
