class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closer = nums[0]

        for i in range(1, len(nums)):
            if abs(nums[i]) <= abs(closer):
                closer = nums[i]

        if closer < 0 and abs(closer) in nums:
            return abs(closer)

        return closer

            