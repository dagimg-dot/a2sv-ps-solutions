class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for out in matrix:
            l = 0
            r = len(out) - 1

            while l <= r:
                mid = (l + r) // 2

                if out[mid] == target:
                    return True

                elif out[mid] > target:
                    r = mid - 1

                elif out[mid] < target:
                    l = mid + 1

        return False