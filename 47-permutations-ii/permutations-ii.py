class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        ans = []

        def dfs(path):
            if len(path) == len(nums):
                ans.append(path[:])
                return
                
            for x in count:
                if count[x] > 0:
                    count[x] -= 1
                    path.append(x)
                    dfs(path)
                    path.pop()
                    count[x] += 1

        dfs([])
        return ans
