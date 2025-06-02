class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        scope = []
        
        def helper(idx, total):
            if total == target:
                ans.append(scope[:])
                return
            
            if total > target:
                return

            for i in range(idx, len(candidates)):
                num = candidates[i]
                scope.append(num)
                helper(i, total + num)  
                scope.pop()

        helper(0, 0)
        return ans