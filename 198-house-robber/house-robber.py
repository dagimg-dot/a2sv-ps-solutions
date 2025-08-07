class Solution:
    def rec(self, i: int, nums: List[int], dp: List[int]) -> int:
        if i >= len(nums):
            return 0
        if dp[i] != -1:
            return dp[i]

        take = nums[i] + self.rec(i + 2, nums, dp)
        dont = self.rec(i + 1, nums, dp)

        dp[i] = max(take, dont)
        return dp[i]

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n
        return self.rec(0, nums, dp)
