class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        modulo = 10**9 + 7

        dp = {-1: 0}

        mon_stack = [-1]

        for i in range(len(arr)):
            while mon_stack!= [-1] and arr[i] <= arr[mon_stack[-1]]:
                mon_stack.pop()

            last = mon_stack[-1]
            
            dp[i] = dp[last] + (i - last) * arr[i]

            mon_stack += [i]

        return sum(dp.values()) % modulo