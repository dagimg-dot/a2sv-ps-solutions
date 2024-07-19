class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l = 0
        r = len(nums) -1

        while l <= r:
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                break
            m = (r + l) // 2
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1

            res = min(res, nums[m])
        
        return res
    