class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            small = i
            for j in range(i, len(nums)):
                if nums[j] < nums[small]:
                    small = j

            nums[i], nums[small] = nums[small], nums[i]

        