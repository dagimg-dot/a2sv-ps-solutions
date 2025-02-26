class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []

        count = Counter(nums)

        for key, value in count.items():
            if value > n // 3:
                ans.append(key)

        return ans
