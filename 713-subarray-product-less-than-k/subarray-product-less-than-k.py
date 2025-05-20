class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans = 0
        beg = 0
        end = 0
        prod =  1

        while end < len(nums):
            prod *= nums[end]
            while end >= beg and prod >= k:
                prod /= nums[beg]
                beg += 1

            ans += end - beg + 1
            end += 1
            
        return ans