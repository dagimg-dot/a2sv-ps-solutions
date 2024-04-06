from typing import List


class Solution():
    def maxLocal(self, sub_grid: List[int], grid: List[List[int]]) -> int:
        local_max = 0

        for i in range(sub_grid[0], sub_grid[1] + 1):
            for j in range(sub_grid[2], sub_grid[3] + 1):
                if grid[i][j] > local_max:
                    local_max = grid[i][j]

        return local_max

    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        max_local_grid = []

        r1 = 0
        r2 = 2
        c1 = 0
        c2 = 2

        while c2 < len(grid) and r2 < len(grid):
            row = []
            while c2 < len(grid) and r2 < len(grid):
                row.append(self.maxLocal([r1, r2, c1, c2], grid))
                c1 += 1
                c2 += 1
            
            max_local_grid.append(row)
            r1 += 1
            r2 += 1
            c1 = 0
            c2 = 2

        return max_local_grid
