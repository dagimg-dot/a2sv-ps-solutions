class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n = len(matrix)
        m = len(matrix[0])

        self.matrix = matrix
        self.presum = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n):
            for j in range(m):
                self.presum[i + 1][j + 1] = (
                    matrix[i][j]
                    + self.presum[i][j + 1]
                    + self.presum[i + 1][j]
                    - self.presum[i][j]
                )

        print(self.presum)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.presum[row2 + 1][col2 + 1]
            - self.presum[row1][col2 + 1]
            - self.presum[row2 + 1][col1]
            + self.presum[row1][col1]
        )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
