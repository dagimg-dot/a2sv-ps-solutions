class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        total = sum(nums[:k])
        avg = total/k

        max_avg = avg

        for i in range(k,n):
            total += nums[i]
            total -= nums[i-k]

            avg = total/k
            max_avg = max(avg, max_avg)

        return max_avg
    