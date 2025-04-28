class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        sl = SortedList()
        ans = 0
        left = 0

        for right in range(n):
            sl.add(nums[right])
            
            while left <= right and sl[-1] - sl[0] > 2:
                sl.remove(nums[left])
                left += 1
            ans += (right-left+1)

        return ans