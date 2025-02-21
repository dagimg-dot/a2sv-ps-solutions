class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True

        not_happy = set()

        isHappy = False

        def digitSquare(num):
            snum = str(num)
            _sum = 0
            for s in snum:
                _sum += int(s)**2

            return _sum


        while n != 1:
            n = digitSquare(n)

            if n == 1:
                isHappy = True
                break

            if n in not_happy:
                break
            else:
                not_happy.add(n)

        return isHappy