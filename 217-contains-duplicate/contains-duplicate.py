class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)
        for value in list(count.values()):
            if value != 1: 
                return True
            
        return False