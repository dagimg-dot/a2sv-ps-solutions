class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pc = Counter(p)
        sc = Counter(s[:len(p)])

        ans = []

        if pc == sc:
            ans.append(0)

        left = 0

        for r in range(len(p), len(s)):
            sc[s[r]] = sc.get(s[r], 0) + 1

            sc[s[left]] -= 1

            if sc[s[left]] == 0:
                sc.pop(s[left])
            
            if sc == pc:
                ans.append(left + 1)
            
            left += 1
        
        return ans

