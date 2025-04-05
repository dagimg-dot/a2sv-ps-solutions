class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainders_found = {}
        curr_sum = 0
        remainders_found[0] = -1

        for i in range(len(nums)):
            curr_sum += nums[i]
            remainder = curr_sum % k

            if remainder in remainders_found:
                if i - remainders_found[remainder] >= 2:
                    return True
            else:
                remainders_found[remainder] = i

        
        return False