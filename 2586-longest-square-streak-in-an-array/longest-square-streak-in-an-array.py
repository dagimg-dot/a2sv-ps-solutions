class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        set_nums = set(nums)
        nums = list(set(nums))
        nums.sort()

        max_count = -1

        for num in nums:
            curr = num
            count = 0
            while curr in set_nums:
                set_nums.remove(curr)
                curr = curr**2
                count += 1
            
            max_count = max(max_count, count)

        return max_count if max_count > 1 else -1
