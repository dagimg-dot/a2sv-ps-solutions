class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        hashmap = {}

        sorted_nums = sorted(nums)

        for i, num in enumerate(sorted_nums):
            if num not in hashmap:
                hashmap[num] = i

        ans = []

        for num in nums:
            ans.append(hashmap[num])

        return ans
 