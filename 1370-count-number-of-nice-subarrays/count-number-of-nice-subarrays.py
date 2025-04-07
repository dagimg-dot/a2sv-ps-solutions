class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l = ans = n_odds = count = 0

        for r in range(len(nums)):
            if nums[r] % 2 != 0:
                n_odds += 1
                count = 0
            
            while n_odds == k:
                count += 1
                if nums[l] % 2 != 0:
                    n_odds -= 1
                
                l += 1
            
            ans += count

        return ans