class Solution:
    def splitString(self, s: str) -> bool:
        def backtrack(prev_value, k):

            if k == len(s):
                return True

            for i in range(k, len(s)):
                cand = int(s[k : i + 1])
                if cand == prev_value - 1:
                    if backtrack(cand, i + 1):
                        return True

            return False

        for i in range(len(s) - 1):
            start = int(s[: i + 1])
            if backtrack(start, i + 1):
                return True

        return False
