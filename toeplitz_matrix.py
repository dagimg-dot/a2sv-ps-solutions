from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        toeplitz = True
        for i in range(len(matrix) - 1):
            for j in range(len(matrix[i]) - 1):
                if j < len(matrix[i]) and i < len(matrix) and matrix[i][j] != matrix[i+1][j+1]:
                    toeplitz = False

        return toeplitz
