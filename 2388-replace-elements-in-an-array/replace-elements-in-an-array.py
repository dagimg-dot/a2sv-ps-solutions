class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        hash_map = defaultdict(int)

        for i in range(len(nums)):
            hash_map[nums[i]] = i
        
        for i, j in operations:
            if i in hash_map:
                hash_map[j] = hash_map.pop(i)

        for i, j in hash_map.items():
            nums[j] = i

        return nums

