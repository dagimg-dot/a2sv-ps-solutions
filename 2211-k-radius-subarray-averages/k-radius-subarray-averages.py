class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        pre_sum = [0] * (n + 1)
        ans = [0] * n

        for i in range(n):
            pre_sum[i + 1] = pre_sum[i] + nums[i]

        for i in range(n):
            s = i - k
            e = i + k

            if s < 0 or e >= n:
                ans[i] = -1
            else:
                ans[i] = (pre_sum[e + 1] - pre_sum[s]) // (2 * k + 1)
            
        return ans