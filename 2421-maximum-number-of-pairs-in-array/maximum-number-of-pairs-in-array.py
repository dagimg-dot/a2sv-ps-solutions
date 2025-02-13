class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        count = Counter(nums)

        pairs = 0
        left = 0
        
        for key, value in count.items():
            pairs += value // 2
            left += value % 2
        
        return [pairs, left]