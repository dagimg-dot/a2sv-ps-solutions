class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ms1 =  Counter(s1)
        ms2 = Counter(s2[:len(s1)])
        l = 0
        for i in range(len(s1),len(s2)):
            if ms1 == ms2:
                return True
            ms2[s2[l]] -= 1
            if ms2[s2[l]] == 0:
                del ms2[s2[l]]
            ms2[s2[i]] += 1
            l += 1
        if ms1 == ms2:
            return True

        return False