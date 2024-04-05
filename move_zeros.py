from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s = 0
        f = 0

        while f < len(nums):
            if nums[f] != 0:
                nums[s], nums[f] = nums[f], nums[s]
                s += 1
            f += 1
