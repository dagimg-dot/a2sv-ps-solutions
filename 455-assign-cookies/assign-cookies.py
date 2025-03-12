class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        j = 0
        for i in range(len(s)):
            if g[j] <= s[i]:
                j += 1
            if j == len(g):
                return j
        
        return j 