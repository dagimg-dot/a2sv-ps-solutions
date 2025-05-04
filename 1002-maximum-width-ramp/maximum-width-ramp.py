class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        def bin_search(arr, idxs, target):
            l, r = 0, len(idxs) - 1
            while l < r:
                m = (l + r) // 2
                if arr[idxs[m]] > target:
                    l = m + 1
                else:
                    r = m

            return idxs[l]

        min_idxs = [0]

        ans = 0
        for i, n in enumerate(nums):
            if n < nums[min_idxs[-1]]:
                min_idxs.append(i)
                continue

            ans = max(ans, i - bin_search(nums, min_idxs, n))

        return ans
