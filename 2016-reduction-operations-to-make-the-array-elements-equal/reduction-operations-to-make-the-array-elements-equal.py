class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        prev = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                prev += 1

            ans += prev

        return ans