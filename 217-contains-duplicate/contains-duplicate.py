class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # count = Counter(nums)
        # for value in list(count.values()):
        #     if value != 1: 
        #         return True
            
        # return False

        seen = {}

        for num in nums:
            if num not in seen:
                seen[num] = 1
            else:
                return True
        
        return False