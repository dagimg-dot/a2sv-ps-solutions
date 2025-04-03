class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)

        ans = 0

        for i in range(0, k):
            if blocks[i] == 'W':
                ans += 1
        
        count = ans

        for i in range(k, n):
            if blocks[i - k] == 'W':
                ans -= 1

            if blocks[i] == 'W':
                ans += 1

            count = ans if ans < count else count

        return count
