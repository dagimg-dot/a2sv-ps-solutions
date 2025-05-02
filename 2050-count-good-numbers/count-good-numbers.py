class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10 ** 9 + 7
        even_pos = n // 2 if n % 2 == 0 else (n + 1) // 2 #
        odd_pos = n // 2

        def binpow(a, b):
            if b == 0:
                return 1
            res = binpow(a, b // 2)
            if b % 2:
                return (res * res * a) % mod
            else:
                return (res * res) % mod
        
        return (binpow(5, even_pos) * binpow(4, odd_pos)) % mod