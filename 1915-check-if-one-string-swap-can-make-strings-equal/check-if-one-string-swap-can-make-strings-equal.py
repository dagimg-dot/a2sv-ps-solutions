class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        count = []

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count.append(i)

        if len(count) == 0:
            return True

        if len(count) == 2 and s1[count[0]] == s2[count[1]] and s1[count[1]] == s2[count[0]]:
            return True

        return False
