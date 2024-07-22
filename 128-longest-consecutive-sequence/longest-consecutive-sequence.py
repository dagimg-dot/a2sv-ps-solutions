class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        nums = sorted(list(set(nums)))
        
        seq = 0
        max_seq = 0

        print(nums)

        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] == 1:
                seq += 1
            else:
                max_seq = max(max_seq, seq)
                seq = 0
        
        return max(max_seq, seq) + 1