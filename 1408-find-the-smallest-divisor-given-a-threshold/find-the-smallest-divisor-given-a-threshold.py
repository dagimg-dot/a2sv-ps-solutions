class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def calc(nums, mid, threshold):
            divisor = 0
            for i in range(len(nums)):
                divisor += math.ceil(nums[i] / mid)
            return divisor

        l = 1
        h = max(nums)
        ans = 0 

        while l <= h:
            mid = l + (h - l) // 2
            if calc(nums, mid, threshold) <= threshold:
                ans = mid
                h = mid - 1
            else:
                l = mid + 1

        return ans