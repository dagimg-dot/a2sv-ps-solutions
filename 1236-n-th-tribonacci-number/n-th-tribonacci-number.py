class Solution:
    def tribonacci(self, n: int) -> int:
        requiredN = n + 3
        array = [0, 1, 1, 2]
        p1, p2, p3 = 1, 2, 3

        if n >= 3:
            for i in range(3, n + 1):
                s = array[p1] + array[p2] + array[p3]
                array.append(s)
                p1 += 1
                p2 += 1
                p3 += 1
            return array[n]

        else:
            return array[n]
