class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = len(nums) + 1
        l, sum = 0, 0
        r = 0
        while r < len(nums):
            sum += nums[r]
            while sum >= target:
                ans = min(ans, r - l + 1)
                sum -= nums[l]
                l += 1

            r += 1

        if ans > len(nums):
            return 0

        return ans