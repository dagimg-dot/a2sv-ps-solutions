class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count = Counter(nums)

        ans = []

        for key, value in count.items():
            if value > 1:
                ans.append(key)

        return ans