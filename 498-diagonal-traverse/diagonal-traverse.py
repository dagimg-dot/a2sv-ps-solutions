class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n, m = len(mat), len(mat[0])

        diagonal_groups = {}

        for i in range(n):
            for j in range(m):
                key = i + j
                if key not in diagonal_groups:
                    diagonal_groups[key] = []
                diagonal_groups[key].append(mat[i][j])

        result = []
        for diagonal_sum, elements in diagonal_groups.items():
            if diagonal_sum % 2 == 0:
                result.extend(elements[::-1])
            else:
                result.extend(elements)

        return result