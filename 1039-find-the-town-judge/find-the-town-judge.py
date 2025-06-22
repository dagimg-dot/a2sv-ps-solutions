class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and not trust:  
            return 1

        trusts_count = [0] * (n + 1)  
        trusted_by = [0] * (n + 1)  

        for a, b in trust:
            trusted_by[a] += 1
            trusts_count[b] += 1 

        for i in range(1, n + 1):
            if trusts_count[i] == n - 1 and trusted_by[i] == 0:
                return i  

        return -1