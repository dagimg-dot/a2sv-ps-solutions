class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1,-1]
        if len(nums) == 0:
            return res

        if target < nums[0] or target > nums[-1]:
            return res

        start = bisect_left(nums, target)
        end = bisect_right(nums, target)

        if nums[start] == target:
            res[0] = start
        
        if nums[end -1] == target:
            res[1] = end - 1
        
        return res