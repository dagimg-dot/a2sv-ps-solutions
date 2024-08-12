class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        nums.sort()
        closer = nums[0]

        for i in range(1, len(nums)):
            if abs(nums[i]) <= abs(closer):
                closer = nums[i]

        return closer

            