class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seen = set()

        ans = []

        for i in range(len(nums)):
            if nums[i] in seen:
                ans.append(nums[i])
            else:
                seen.add(nums[i])

        return ans
            
