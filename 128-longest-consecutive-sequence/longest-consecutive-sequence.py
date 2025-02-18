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

        # if nums == []:
        #     return 0

        # st = set(nums)
        # longest = 1

        # for n in st:
        #     if n - 1 in st:
        #         count = 1
        #         x = n

        #         while x + 1 in st:
        #             count += 1
        #             x += 1
                
        #         longest = max(longest, count)
            
        # return longest + 1
