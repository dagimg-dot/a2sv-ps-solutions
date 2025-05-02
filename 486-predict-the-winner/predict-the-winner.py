class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def get_score(left, right): 
            if left > right:
                return 0
            
            left_score = nums[left] - get_score(left + 1, right)
            right_score = nums[right] - get_score(left, right - 1)

            return max(left_score, right_score)
        
        return get_score(0, len(nums) - 1) >= 0

