class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def count(d):
            n = 1
            x = position[0]
            
            for y in position:
                if y - x > d:
                    x = y
                    n += 1
            return n

        return bisect_left(range(position[-1] - position[0]), True, key=lambda d: count(d) < m)