class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()

        for i in range(len(nums)):
            target = -nums[i]
            hash_map = {}

            for j in range(i + 1, len(nums)):
                num = hash_map.get(target - nums[j])
                if num is not None:
                    ans.add((nums[i], target - nums[j], nums[j]))
                else:
                    hash_map[nums[j]] = j

        return [list(triplet) for triplet in ans]