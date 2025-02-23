class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        l = 0

        while l < len(nums) - 1:
            if nums[l] == nums[l + 1]:
                nums[l] *= 2
                nums[l + 1] = 0
                l += 2
            else:
                l += 1

        z = nums.count(0)
        nums = [i for i in nums if i != 0]
        nums = nums + ([0] * z)
        
        return nums


        