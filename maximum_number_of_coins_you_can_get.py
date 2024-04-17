from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles) - len(piles) // 3
        piles.sort(reverse=True)

        ans = 0
        for i in range(len(piles)):
            if i % 2 == 1 and i < n:
                ans += piles[i]

        return ans
