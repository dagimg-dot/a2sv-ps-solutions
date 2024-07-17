class Solution:
    def myPow(self, x: float, n: int) -> float:
        powered = 1
        if x in [1,-1]:
            if n % 2 == 0:
                return abs(x)
            else:
                return x
        if n <= -(2**31) or n >= (2**31 - 1):
            return 0
        sign = 1 if n > 0 else -1
        n = abs(n)

        for i in range(n): 
            if sign == 1:
                powered *= x
            else:
                powered *= (1/x)

        return powered if powered >= -(10**4) and powered <= (10**4) else 0
        