class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count = Counter(p)
        s_count = Counter(s[:len(p)])

        ans = []

        if p_count == s_count:
            ans.append(0)

        left = 0
        
        for r in range(len(p), len(s)):
            s_count[s[r]] = s_count.get(s[r], 0) + 1

            s_count[s[left]] -= 1

            if s_count[s[left]] == 0:
                s_count.pop(s[left])

            if p_count == s_count:
                ans.append(left+1)
            
            left += 1

        return ans

