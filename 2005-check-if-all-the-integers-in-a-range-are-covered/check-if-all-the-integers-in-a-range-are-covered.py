class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for i in range(left, right + 1):
            is_covered = False

            for r in ranges:
                if r[0] <= i <= r[1]:
                    is_covered = True
                    break

            if not is_covered:
                return False
            
        return True