class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            cand = numbers[l] + numbers[r]
            if cand == target:
                return [l+1, r+1]
            elif cand < target:
                l += 1
            else:
                r -= 1

            