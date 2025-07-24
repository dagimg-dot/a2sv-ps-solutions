class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        fresh = 0
        mins = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r, c])

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while q and fresh > 0:
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc

                    if r not in range(rows) or c not in range(cols) or grid[r][c] != 1:
                        continue
                    grid[r][c] = 2
                    q.append([r, c])
                    fresh -= 1
            mins += 1

        return mins if fresh == 0 else -1
