class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n, m = len(mat), len(mat[0])

        diagonal_sums = defaultdict(list)

        for i in range(n):
            for j in range(m):
                diagonal_sums[i+j].append(mat[i][j])

        
        result = []
        for diagonal_sum, elements in diagonal_sums.items():
            if diagonal_sum % 2 == 0:
                result.extend(elements[::-1])
            else:
                result.extend(elements)

        return result