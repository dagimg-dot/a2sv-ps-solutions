class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])

        result = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                result[i][j] = matrix[j][i]

        return result 