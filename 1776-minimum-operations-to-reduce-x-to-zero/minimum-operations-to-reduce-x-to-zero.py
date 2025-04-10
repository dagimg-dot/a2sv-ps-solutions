class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        t = sum(nums) - x

        if t == 0:
            return n

        max_len = cur_sum = l = 0

        for r in range(n):
            cur_sum += nums[r]
            
            while l <= r and cur_sum > t:
                cur_sum -= nums[l]
                l += 1
            
            if cur_sum == t:
                max_len = max(max_len, r - l + 1)
            
        return n - max_len if max_len else -1
        