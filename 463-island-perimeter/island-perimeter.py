class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n = len(grid)
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    x = 4
                    if i > 0 and grid[i - 1][j] == 1:
                        x -= 1
                    if j > 0 and grid[i][j - 1] == 1:
                        x -= 1
                    if i < n - 1 and grid[i + 1][j] == 1:
                        x -= 1
                    if j < len(grid[i]) - 1 and grid[i][j + 1] == 1:
                        x -= 1
                    count += x

        return count
