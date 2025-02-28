class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = 0
        net_count = 0
        min_value = float('inf')
        
        for row in matrix:
            for value in row:
                total += abs(value)
                if value < 0:
                    net_count += 1
                min_value = min(min_value, abs(value))

        if net_count % 2 == 1:
            total -= 2 * min_value
        
        return total