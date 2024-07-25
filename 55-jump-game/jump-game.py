class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1

        for i in reversed(range(len(nums))):
            if nums[i] + i >= target:
                target = i
        
        return target == 0


