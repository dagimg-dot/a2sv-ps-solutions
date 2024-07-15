class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_ones = 0
        n_zeros = 0
        l = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                n_zeros += 1
            
            while n_zeros > k:
                if nums[l] == 0:
                    n_zeros -= 1
                l += 1
            
            max_ones = max(max_ones, r - l + 1)
        
        return max_ones
                