class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        count = 0

        for p in points:
            hash_map = {}

            for q in points:
                f = p[0]-q[0]
                s = p[1]-q[1]
                hash_map[f*f + s*s] = 1 + hash_map.get(f*f + s*s, 0)

            for k in hash_map:
                count += hash_map[k] * (hash_map[k] -1)

        return count