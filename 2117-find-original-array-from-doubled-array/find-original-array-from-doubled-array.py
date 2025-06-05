class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort() # 1,2,3,4,6,8
        zeros = changed.count(0)
        final = []
        if zeros % 2 == 0:
            final = [0] * (zeros // 2)
            if zeros != len(changed):
                changed = changed[zeros:]
            else:
                return final
        else:
            return []
        
        counts = {}
        for elt in changed:
            if elt in counts:
                counts[elt] += 1
            else:
                counts[elt] = 1

        for elt in counts:
            if counts[elt] > 0 and elt*2 in counts and counts[elt*2] > 0:
                pairs = min(counts[elt], counts[elt*2])
                final += [elt] * pairs
                counts[elt] -= pairs
                counts[elt*2] -= pairs

        for elt in counts:
            if counts[elt] != 0:
                return []

        return final