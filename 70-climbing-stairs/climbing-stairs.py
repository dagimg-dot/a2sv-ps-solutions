class Solution:
    def climbStairs(self, n: int) -> int:
        def finddp(i, dp):
            if dp[i] != -1:
                return dp[i]
            if i == 1:
                dp[i] = 1
            elif i == 2:
                dp[i] = 2
            else:
                dp[i] = finddp(i - 1, dp) + finddp(i - 2, dp)
            return dp[i]

        dp = [-1] * (n + 1)
        return finddp(n, dp)
