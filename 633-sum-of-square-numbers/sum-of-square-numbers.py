class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        prime_factorization = {}
        if c in [0,1]:
            return True
        for i in range(2, int(math.sqrt(c))+1):
            while c % i == 0:
                if i in prime_factorization.keys():
                    prime_factorization[i] += 1
                else:
                    prime_factorization[i] = 0
                    prime_factorization[i] += 1
                c //= i
        if c > 2:
                prime_factorization[c] = 0
                prime_factorization[c] += 1
        for p, a in prime_factorization.items():
            if p % 4 == 3 and a % 2 != 0:
                return False

        return True
        
        