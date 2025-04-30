class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337

        n = int(''.join(map(str, b)))

        def pow(x, n):
            if n == 1:
                return x

            pow2 = pow(x, n // 2) % MOD

            if n % 2 == 0:
                return pow2 * pow2 % MOD
            else:
                return x * pow2 * pow2 % MOD

        return pow(a, n) % MOD


        