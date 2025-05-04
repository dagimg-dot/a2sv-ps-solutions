class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        t = float('-inf')
        
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < t:
                return True
            while stack and stack[-1] < nums[i]:
                t = stack.pop()
            stack.append(nums[i])
        
        return False