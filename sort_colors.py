from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def select(arr, i):
            small = i
            for j in range(i, len(arr)):
                if arr[j] < arr[small]:
                    small = j
            return small

        for i in range(len(nums)):
            smallest = select(nums, i)
            nums[i], nums[smallest] = nums[smallest], nums[i]
