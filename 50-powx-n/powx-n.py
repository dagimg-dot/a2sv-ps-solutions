class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 1:
            return x

        return pow(x, n)
        