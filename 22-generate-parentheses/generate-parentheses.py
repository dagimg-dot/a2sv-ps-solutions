class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(current: str, left: int, right: int):
            if len(current) == 2 * n:
                ans.append(current)
                return
            if left < n:
                backtrack(current + '(', left + 1, right)
            if right < left:
                backtrack(current + ')', left, right + 1)

        backtrack('', 0, 0)
        
        return ans