class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        freq = Counter()

        ans = total = count = 0

        for num in nums:
            total += freq[num]
            freq[num] += 1

            while total >= k:
                freq[nums[count]] -= 1
                total -= freq[nums[count]]
                count += 1

            ans += count

        return ans