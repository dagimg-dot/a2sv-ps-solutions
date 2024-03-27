from typing import List


class Solution:
    def similarPairs(self, words: List[str]) -> int:
        hash_map = {}

        for word in words:
            w = sorted(set(word))
            w = ''.join(w)

            hash_map[w] = hash_map.get(w, 0) + 1

        count = 0

        for word in hash_map:
            c = hash_map[word]
            count += (c*(c-1)) // 2

        return count
