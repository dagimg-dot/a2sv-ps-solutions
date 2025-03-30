class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = m_score = c_score = 0
        counter = defaultdict(int)
        n = len(nums)

        for right in range(n):
            right_num = nums[right]
            c_score += right_num
            counter[right_num] += 1

            while counter[right_num] > 1:
                left_num = nums[left]
                c_score -= left_num
                counter[left_num] -= 1
                left += 1

            m_score = max(m_score, c_score)
        
        return m_score     