class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        max_found, l, r, count = 0, 0, 0, 0

        while r < len(s) - 1:
            if s[r] == s[r + 1]:
                count += 1

            while count >= 2:
                max_found = max(max_found, r - l + 1)
                if s[l] == s[l + 1]:
                    count -= 1
                
                l += 1
            r += 1
        
        return max(max_found, r - l + 1)

