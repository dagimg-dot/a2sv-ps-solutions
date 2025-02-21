class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()

        def multiply(numss):
            product = 1

            for num in numss:
                product *= num

            return product

        alt = nums[:2]
        alt.extend(nums[-1:])

        return max(multiply(nums[-3:]), multiply(alt))