class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        freq = [0] * k
        freq[0] = 1
        curr_sum = 0
        count = 0

        for i in range(len(nums)):
            curr_sum += nums[i]

            remainder = curr_sum % k

            if remainder < 0:
                remainder += k
            
            count += freq[remainder]
            freq[remainder] += 1
        
        return count