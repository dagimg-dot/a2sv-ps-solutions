class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count = 0
        ab = defaultdict(int)

        for num1 in nums1:
            for num2 in nums2:
                key = num1 + num2
                ab[key] += 1

        for num3 in nums3:
            for num4 in nums4:
                key = -(num3 + num4)
                if key in ab:
                    count += ab[key]

        return count


                