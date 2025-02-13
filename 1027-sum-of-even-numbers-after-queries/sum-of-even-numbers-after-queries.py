class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = sum(num for num in nums if num % 2 == 0)

        ans = []

        for v, i in queries:
            if nums[i] % 2 == 0:
                even_sum -= nums[i]
            
            nums[i] += v

            if nums[i] % 2 == 0:
                even_sum += nums[i]
            
            ans.append(even_sum)
        
        return ans




