class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        steps = {
            1: [({1, 4, 6}, 0, -1), ({1, 3, 5}, 0, 1)],
            2: [({2, 3, 4}, -1, 0), ({2, 5, 6}, 1, 0)],
            3: [({5, 6, 2}, 1, 0), ({4, 6, 1}, 0, -1)],
            4: [({5, 6, 2}, 1, 0), ({3, 5, 1}, 0, 1)],
            5: [({3, 2, 4}, -1, 0), ({6, 1, 4}, 0, -1)],
            6: [({3, 4, 2}, -1, 0), ({5, 3, 1}, 0, 1)],
        }

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        seen = set([(0, 0)])
        queue = deque([(0, 0, grid[0][0])])

        while queue:

            n = len(queue)

            for _ in range(n):

                row, col, state = queue.popleft()

                if row == len(grid) - 1 and col == len(grid[0]) - 1:
                    return True

                for allowed, r, c in steps[grid[row][col]]:
                    if (
                        0 <= row + r <= len(grid) - 1
                        and 0 <= col + c <= len(grid[0]) - 1
                    ):
                        if (row + r, col + c) not in seen:
                            if grid[row + r][col + c] in allowed:
                                queue.append((row + r, col + c, grid[row + r][col + c]))
                                seen.add((row + r, col + c))

        return False
