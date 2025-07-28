class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        res = []

        for r in matrix:
            res += r

        return sorted(res)[k - 1]
