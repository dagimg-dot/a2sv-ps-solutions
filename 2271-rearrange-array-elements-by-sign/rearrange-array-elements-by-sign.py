class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = [p for p in nums if p > 0]
        neg = [n for n in nums if n < 0]

        ans = []

        for i in range(len(pos)):
            ans.append(pos[i])
            ans.append(neg[i])

        return ans

        

