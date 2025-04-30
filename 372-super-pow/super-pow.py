class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        if a == 1:
            return a

        n = int(''.join(map(str, b)))

        return pow(a, n, 1337)


        