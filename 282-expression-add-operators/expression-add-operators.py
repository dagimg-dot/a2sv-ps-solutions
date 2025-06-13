class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        ans = []
        n = len(num)

        def dfs(index, prevOpe, currVal, expr):
            if index == n:
                if currVal == target:
                    ans.append(expr)
                return
            for i in range(index, n):
                if i != index and num[index] == "0":
                    break
                currStr = num[index : i + 1]
                curr = int(currStr)
                if index == 0:
                    dfs(i + 1, curr, curr, currStr)
                else:
                    dfs(i + 1, curr, currVal + curr, expr + "+" + currStr)
                    dfs(i + 1, -curr, currVal - curr, expr + "-" + currStr)
                    dfs(
                        i + 1,
                        prevOpe * curr,
                        currVal - prevOpe + prevOpe * curr,
                        expr + "*" + currStr,
                    )

        dfs(0, 0, 0, "")
        return ans
