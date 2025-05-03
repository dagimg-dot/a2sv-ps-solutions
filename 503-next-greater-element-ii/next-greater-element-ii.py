class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        stack = []

        for i in range(2*n-1, -1, -1):
            num = nums[i % n]

            while stack and stack[-1] <= num:
                stack.pop()

            if stack:
                ans[i % n] = stack[-1]
            
            stack.append(num)

        return ans