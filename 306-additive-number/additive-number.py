class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def backtrack(i, prev, curr, cnt):
            if i >= len(num):
                return cnt >= 3

            if cnt < 2:
                for ind in range(i, len(num)):
                    s = num[i:(ind + 1)]
                    if len(s) > 1 and s.startswith("0"):
                        continue
                    if backtrack(ind + 1, curr, int(s), cnt + 1):
                        return True
            else:
                for ind in range(i, len(num)):
                    s = num[i:(ind + 1)]
                    if len(s) > 1 and s.startswith("0"):
                        continue
                    if prev + curr == int(s) and backtrack(ind + 1, curr, int(s), cnt + 1):
                        return True

            return False
            
        return backtrack(0, None, None, 0)